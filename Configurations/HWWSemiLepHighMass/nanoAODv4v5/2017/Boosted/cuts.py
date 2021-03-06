#import my.Wlep_sel
#import my.final_fatjetsel



supercut = 'nLepton>0'


#-----Variable Deinition-----#




eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

METtype='Puppi'

if METtype=='' or METtype=='PF': 
    MET_pt='MET_pt'
    MET_phi='MET_phi'
    Wlep_px='Wlep_px_PF'
    Wlep_py='Wlep_py_PF'
    Wlep_pz='Wlep_pz_PF'
    Wlep_E='Wlep_E_PF'
    Wlep_pt='Wlep_pt_PF'
    Wlep_eta='Wlep_eta_PF'
    Wlep_phi='Wlep_phi_PF'
    Wlep_mass='Wlep_mass_PF'


else:
    MET_pt=METtype+'MET_pt'
    MET_phi=METtype+'MET_phi'
    Wlep_px='Wlep_px_'+METtype
    Wlep_py='Wlep_py_'+METtype
    Wlep_pz='Wlep_pz_'+METtype
    Wlep_E='Wlep_E_'+METtype
    Wlep_pt='Wlep_pt_'+METtype
    Wlep_eta='Wlep_eta_'+METtype
    Wlep_phi='Wlep_phi_'+METtype
    Wlep_mass='Wlep_mass_'+METtype


LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'

bAlgo='DeepB'
bWP='0.2219'

isbjet='(CleanJet_jetIdx[CleanJetNotFat_jetIdx]>0 && CleanJet_pt[CleanJetNotFat_jetIdx]>20 && fabs(CleanJet_eta[CleanJetNotFat_jetIdx]) < 2.4 && Jet_btag'+bAlgo+'[CleanJet_jetIdx[CleanJetNotFat_jetIdx]] > '+bWP+'  )'
nbjet='(Sum$'+isbjet+')'
btagSF_each='( '+isbjet+'*Alt$(Jet_btagSF_shape, 1) + !'+isbjet+'*1 )'
logbtagSF='(Sum$(  TMath::Log('+btagSF_each+')))'
btagSF='(TMath::Exp( '+logbtagSF+' ))'


ww_px_pow2=' pow(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_px+', 2    )'
ww_px='(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_px+')'
ww_py_pow2=' pow(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_py+', 2    )'
ww_py='(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_py+')'
ww_pz_pow2=' pow(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_pz+', 2    )'
ww_pz='(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_pz+')'
ww_E_pow2=' pow(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_E+', 2    )'
ww_E='(     CleanFatJet_pt[0]*cos(CleanFatJet_phi[0])+'+Wlep_E+')'

mww = '( sqrt( '+ww_E_pow2+' - '+ww_px_pow2+' - '+ww_py_pow2+' -'+ww_pz_pow2+'    )     )'
ww_pt='( sqrt( '+ww_px_pow2+' + '+ww_py_pow2+'  )  )'
ww_phi = '(atan('+ww_py+'/'+ww_px+' ) )'
ww_eta=' ( asinh('+ww_pz+'/'+ww_pt+') )'

#------End of Variable Definition-----#




cuts['1FatJetM40']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\

cuts['1FatJetM40__bevent']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'

cuts['1FatJetM40__bvetoevent']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'


cuts['1FatJetM40__bevent__massSB']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(CleanFatJet_mass[0]< 65 || ( CleanFatJet_mass[0]<250 && CleanFatJet_mass[0]>105 ) )'


cuts['1FatJetM40__bvetoevent__massSB']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13)))  )'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(CleanFatJet_mass[0]< 65 || ( CleanFatJet_mass[0]<250 && CleanFatJet_mass[0]>105 ) )'


cuts['1FatJetM40_bevent_massSR']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(CleanFatJet_mass[0]>65 && CleanFatJet_mass[0]<105  )'


cuts['1FatJetM40_bvetoevent_massSR']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(CleanFatJet_mass[0]>65 && CleanFatJet_mass[0]<105  )'




cuts['1FatJetM40_bevent_massSR_ptw_over_mww04']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(CleanFatJet_mass[0]>65 && CleanFatJet_mass[0]<105  )'+'&&'\
    +'(min('+Wlep_pt+',CleanFatJet_pt)/('+mww+') > 0.4)'


cuts['1FatJetM40_bvetoevent_massSR_ptw_over_mww04']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(CleanFatJet_mass[0]>65 && CleanFatJet_mass[0]<105  )'+'&&'\
    +'(min('+Wlep_pt+',CleanFatJet_pt)/('+mww+') > 0.4)'




cuts['1FatJetM40_bevent_massSB_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(CleanFatJet_mass[0]<65 || ( CleanFatJet_mass[0]<250 && CleanFatJet_mass[0]>105 )  )'+'&&'\
    +'(CleanFatJet_tau21 < 0.4)'


cuts['1FatJetM40_bvetoevent_massSB_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(CleanFatJet_mass[0]<65 || ( CleanFatJet_mass[0]<250 && CleanFatJet_mass[0]>105 )  )'+'&&'\
    +'(CleanFatJet_tau21 < 0.4)'


cuts['1FatJetM40_bevent_massSR_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(CleanFatJet_mass[0]>65 && CleanFatJet_mass[0]<105  )'+'&&'\
    +'(CleanFatJet_tau21 < 0.4)'

cuts['1FatJetM40_bvetoevent_massSR_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(CleanFatJet_mass[0]>65 && CleanFatJet_mass[0]<105  )'+'&&'\
    +'(CleanFatJet_tau21 < 0.4)'


cuts['1FatJetM40_bevent_massSR_ptw_over_mww_04_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'>0)'+'&&'\
    +'(CleanFatJet_mass[0]>65 && CleanFatJet_mass[0]<105  )'+'&&'\
    +'(CleanFatJet_tau21 < 0.4)'+'&&'\
    +'(min('+Wlep_pt+',CleanFatJet_pt)/('+mww+') > 0.4)'


cuts['1FatJetM40_bvetoevent_massSR_ptw_over_mww_04_tau21']='(  Lepton_pt[0]>30 && fabs(Lepton_eta[0])  < (2.1*(abs(Lepton_pdgId[0])==11) + 2.4*(abs(Lepton_pdgId[0]==13))))'+'&&'\
    +LepWPCut+'&&'\
    +'( Alt$( Lepton_pt[1],-1) < 15*( abs(Lepton_pdgId[0])==11  ) + 10*(abs(Lepton_pdgId[0]))==13   )'+'&&'\
    +'( '+MET_pt+' > 40 )'+'&&'\
    +'(nCleanFatJet==1)'+'&&'\
    +'('+nbjet+'==0)'+'&&'\
    +'(CleanFatJet_mass[0]>65 && CleanFatJet_mass[0]<105  )'+'&&'\
    +'(CleanFatJet_tau21 < 0.4)'+'&&'\
    +'(min('+Wlep_pt+',CleanFatJet_pt)/('+mww+') > 0.4)'

