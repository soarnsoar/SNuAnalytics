import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import math, re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict


class BinByBinJERMaker(Module):
    def __init__(self, jetType = "AK8PFPuppi", noGroom = False, jer_bin_list = [ 0, 1 ], metBranchName="MET" ):
      if "AK4" in jetType : 
        self.jetBranchName = "Jet"
        self.doGroomed = noGroom
        self.doMET = True
      elif "AK8" in jetType :
        self.jetBranchName = "FatJet"
        self.doGroomed = not noGroom
        self.doMET = False
      else:
        raise ValueError("ERROR: Invalid jet type = '%s'!" % jetType)
      self.lenVar = "n" + self.jetBranchName

      self.jer_bin_list = jer_bin_list
      if self.doMET : 
        self.metBranchName = metBranchName
        self.unclEnThreshold = 15.

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.itree = inputTree
        
        #new branch
        for shift in [ "Up", "Down" ]:
          for binIdx in self.jer_bin_list:
            self.out.branch("%s_pt_jer%s%s" % (self.jetBranchName, binIdx, shift), "F", lenVar=self.lenVar)
            self.out.branch("%s_mass_jer%s%s" % (self.jetBranchName, binIdx, shift), "F", lenVar=self.lenVar)
            if self.doGroomed:
              self.out.branch("%s_msoftdrop_jer%s%s" % (self.jetBranchName, binIdx, shift), "F", lenVar=self.lenVar)
              self.out.branch("%s_msoftdrop_tau21DDT_jer%s%s" % (self.jetBranchName, binIdx, shift), "F", lenVar=self.lenVar)

            if self.doMET : 
              self.out.branch("%s_pt_jer%s%s" % (self.metBranchName, binIdx, shift), "F")
              self.out.branch("%s_phi_jer%s%s" % (self.metBranchName, binIdx, shift), "F")

        self.isV5NanoAOD = hasattr(inputTree, "Jet_muonSubtrFactor")
        print "nanoAODv5?", self.isV5NanoAOD

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        jets  = Collection(event, self.jetBranchName)
        if self.doMET : 
          muons     = Collection(event, "Muon" ) # to subtract out of the jets for proper type-1 MET corrections
          met_pt_jer   = event.getattr(self.metBranchName+"_pt_jer")
          met_phi_jer  = event.getattr(self.metBranchName+"_phi_jer")
          met_px_jer   = met_pt_jer*math.cos(met_phi_jer)
          met_py_jer   = met_pt_jer*math.sin(met_phi_jer)
          met_px_jer_shift   = met_px_jer
          met_py_jer_shift   = met_py_jer

        OutBranchs = {}
        for shift in [ "Up", "Down" ]:
          for binIdx in self.jer_bin_list:
            OutBranchs["%s_pt_jer%s%s" % (self.jetBranchName, binIdx, shift)]   = []
            OutBranchs["%s_mass_jer%s%s" % (self.jetBranchName, binIdx, shift)] = []
            if self.doGroomed:
              OutBranchs["%s_msoftdrop_jer%s%s" % (self.jetBranchName, binIdx, shift)]          = []
              OutBranchs["%s_msoftdrop_tau21DDT_jer%s%s" % (self.jetBranchName, binIdx, shift)] = []

            if self.doMET : 
              OutBranchs["%s_pt_jer%s%s" % (self.metBranchName, binIdx, shift)]  = met_pt_jer
              OutBranchs["%s_phi_jer%s%s" % (self.metBranchName, binIdx, shift)] = met_phi_jer

        for jet in jets:
          jet_eta     = jet['eta']
          jet_pt      = jet['pt']

          if self.doMET : 
            jet_rawpt   = jet['pt_raw']
            jet_pt_orig = jet_pt

            jec   = jet_pt/jet_rawpt

            # get the jet for type-1 MET
            newjet = ROOT.TLorentzVector()
            if self.isV5NanoAOD:
                newjet.SetPtEtaPhiM(jet_pt_orig*(1-jet.rawFactor)*(1-jet.muonSubtrFactor), jet.eta, jet.phi, jet.mass )
                muon_pt = jet_pt_orig*(1-jet.rawFactor)*jet.muonSubtrFactor
            else:
                newjet.SetPtEtaPhiM(jet_pt_orig*(1-jet.rawFactor), jet.eta, jet.phi, jet.mass )
                muon_pt = 0
                if hasattr(jet, 'muonIdx1'):
                  if jet.muonIdx1>-1:
                      if muons[jet.muonIdx1].isGlobal:
                        newjet = newjet - muons[jet.muonIdx1].p4()
                        muon_pt += muons[jet.muonIdx1].pt
                  if jet.muonIdx2>-1:
                      if muons[jet.muonIdx2].isGlobal:
                        newjet = newjet - muons[jet.muonIdx2].p4()
                        muon_pt += muons[jet.muonIdx2].pt

            # set the jet pt to the muon subtracted raw pt
            jet.pt = newjet.Pt()
            # get the proper jet pts for type-1 MET. only correct the non-mu fraction of the j
            jet_pt_noMuL1L2L3 = jet.pt*jec    if jet.pt*jec > self.unclEnThreshold else jet.pt
             
            ## setting jet back to central values
            jet.pt          = jet_pt

            jet_pt_L1L2L3   = jet_pt_noMuL1L2L3 + muon_pt

          jerSystBinIdx = self.GetJERSystBin(jet_eta, jet_pt)
          #
          for shift in [ "Up", "Down" ]:
            for binIdx in self.jer_bin_list:
              if binIdx == jerSystBinIdx:
                pt_jer   = jet['pt_jer%s'%shift]
                mass_jer = jet['mass_jer%s'%shift]
                if self.doGroomed:
                  msoftdrop_jer          = jet['msoftdrop_jer%s'%shift]
                  msoftdrop_tau21DDT_jer = jet['msoftdrop_tau21DDT_jer%s'%shift]
              else:
                pt_jer   = jet['pt_nom']
                mass_jer = jet['mass_nom']
                if self.doGroomed:
                  msoftdrop_jer          = jet['msoftdrop_nom']
                  msoftdrop_tau21DDT_jer = jet['msoftdrop_tau21DDT_nom']

              OutBranchs["%s_pt_jer%s%s" % (self.jetBranchName, binIdx, shift)].append(pt_jer)
              OutBranchs["%s_mass_jer%s%s" % (self.jetBranchName, binIdx, shift)].append(mass_jer)
              if self.doGroomed:
                OutBranchs["%s_msoftdrop_jer%s%s" % (self.jetBranchName, binIdx, shift)].append(msoftdrop_jer)
                OutBranchs["%s_msoftdrop_tau21DDT_jer%s%s" % (self.jetBranchName, binIdx, shift)].append(msoftdrop_tau21DDT_jer)


              if self.doMET : 
                if jet_pt_L1L2L3 > self.unclEnThreshold and (jet.neEmEF+jet.chEmEF) < 0.9:
                    if not ( self.metBranchName == 'METFixEE2017' and 2.65<abs(jet_eta)<3.14 and jet_pt*(1-jet.rawFactor)<50 ): # do not re-correct for jets that aren't included in METv2 recipe
                        jet_cosPhi = math.cos(jet.phi)
                        jet_sinPhi = math.sin(jet.phi)

                        if binIdx == jerSystBinIdx:
                          met_px_jer_shift += jet_pt_L1L2L3*(1 - pt_jer/(jet["corr_JEC"]*jet_rawpt) )*jet_cosPhi 
                          met_py_jer_shift += jet_pt_L1L2L3*(1 - pt_jer/(jet["corr_JEC"]*jet_rawpt) )*jet_sinPhi 
                        else:
                          pass

        if self.doMET : 
          OutBranchs["%s_pt_jer%s%s" % (self.metBranchName, binIdx, shift)]  = math.sqrt(met_px_jer_shift**2+met_py_jer_shift**2)
          OutBranchs["%s_phi_jer%s%s" % (self.metBranchName, binIdx, shift)] = math.atan2(met_py_jer_shift, met_px_jer_shift)

        #
        for OutBranchName, OutBranch in OutBranchs.iteritems():
          self.out.fillBranch(OutBranchName, OutBranch)

        return True


    def GetJERSystBin(self, eta, pt):
        # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetResolution#Run2_JER_uncertainty_correlation
        # - in region |eta| < 1.93 use one pT bin: (0,Inf) 
        # - in region 1.93 < |eta| < 2.5 use one pT bin: (0,Inf) 
        # - in region 2.5 < |eta| < 3 use two pT bins: (0,50) and (50,Inf) 
        # - in region 3 < |eta| < 5 use two pT bins: (0,50) and (50,Inf)

        absEta = abs(eta)

        if absEta < 1.93:
          jerSystBinIdx = 0
        elif 1.93 < absEta < 2.50:
          jerSystBinIdx = 1
        elif 2.50 < absEta < 3.00:
          if pt < 50:
            jerSystBinIdx = 2
          else:
            jerSystBinIdx = 3
        elif 3.00 < absEta < 5.00:
          if pt < 50:
            jerSystBinIdx = 4
          else:
            jerSystBinIdx = 5
        else:
            jerSystBinIdx = -1
            print(" [WARNING] GetJERSystBin : eta range out of bound, eta : %.2f"%eta)

        return jerSystBinIdx

