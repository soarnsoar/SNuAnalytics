#import my.Wlep_sel
#import my.final_fatjetsel



#supercut = 'nCleanFatJet==1'



#-----Variable Deinition-----#


Year='2016'

eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'


LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepPtCut='(Lepton_pt[0] > 30*(abs(Lepton_pdgId[0])==11))'




#------End of Variable Definition-----#
supercut = LepWPCut+'&&'+LepPtCut

LepCats={}
LepCats['']='(1)'
LepCats['ElectronCh']='(abs(Lepton_pdgId[0])==11)'
LepCats['MuonCh']='(abs(Lepton_pdgId[0])==13)'


BoostCats={}
BoostCats['BoostedSR']='IsBoostedSR'
#BoostCats['BoostedSB']='IsBoostedSB'
#BoostCats['BoostedTop']='IsBoostedTopCR'
    
BoostProcCats={}
BoostProcCats['']='1'
BoostProcCats['ggf']='!IsVbfFat'
BoostProcCats['vbf']='IsVbfFat'


ResolveCats={}
ResolveCats['ResolvedSR']='IsResolvedSR'
#ResolveCats['ResolvedSB']='IsResolvedSB'
#ResolveCats['ResolvedTop']='IsResolvedTopCR'
    
ResolveProcCats={}
ResolveProcCats['']='1'
ResolveProcCats['ggf']='!IsVbfjj'
ResolveProcCats['vbf']='IsVbfjj'




##===Define cuts===###
for Lep in LepCats:
    


    for BCat in BoostCats: 
        for BProcCat in BoostProcCats:
            cuts[Lep+BProcCat+BCat+Year]=BoostCats[BCat]\
                +'&&'+BoostProcCats[BProcCat]\
                +'&&'+LepCats[Lep]

    for RCat in ResolveCats: 
        for RProcCat in ResolveProcCats:
            cuts[Lep+RProcCat+RCat+Year]=ResolveCats[RCat]\
                +'&&'+ResolveProcCats[RProcCat]\
                +'&&'+LepCats[Lep]

