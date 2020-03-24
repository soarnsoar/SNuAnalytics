
#source TurnOnDryRun.sh
SAMPLES=()
SAMPLES=(
SingleElectron_Run2017B-Nano1June2019-v1
SingleElectron_Run2017C-Nano1June2019-v1
SingleElectron_Run2017D-Nano1June2019-v1
SingleElectron_Run2017E-Nano1June2019-v1
SingleElectron_Run2017F-Nano1June2019-v1
SingleMuon_Run2017B-Nano1June2019-v1
SingleMuon_Run2017C-Nano1June2019-v1
SingleMuon_Run2017D-Nano1June2019-v1
SingleMuon_Run2017E-Nano1June2019-v1
SingleMuon_Run2017F-Nano1June2019-v1
)
EXCLUDE=()

#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done
#echo ${SAMPLE_LIST}
#echo ${EXCLUDE_LIST}


#mkPostProc.py -p Run2017_102X_nAODv5_Full2017v6 -i Prod -s DATAl1loose2017v6 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Run2017_102X_nAODv5_Full2017v6 -i DATAl1loose2017v6 -s HMSemilepSkimJHv6_7_data -b -T ${SAMPLE_LIST}


#mkPostProc.py -p Run2017_102X_nAODv5_Full2017v6 -i DATAl1loose2017v6__HMSemilepSkimJHv6_7_data -s HMlnjjVars_Dev_jhchoi5 -b -T ${SAMPLE_LIST}

#mkPostProc.py -p Run2017_102X_nAODv5_Full2017v6 -i DATAl1loose2017v6 -s HMSemilepSkimJHv6_7_data -b -T SingleMuon_Run2017D-Nano1June2019-v1

##--Fake
#mkPostProc.py -p Run2017_102X_nAODv5_Full2017v6 -i DATAl1loose2017v6__HMSemilepSkimJH2017v6_5_data -s fakeWstep1l -b -T ${SAMPLE_LIST}





##---Fake
modcfg="--modcfg SNuAnalytics/NanoGardenerFrameworks/HWWSemilepHM/20200316_Fake/Steps_cfg.py"

mkPostProc.py $modcfg -p Run2017_102X_nAODv5_Full2017v6 -i DATAl1loose2017v6__HMSemilepSkimJHv6_7_data -s HMSemilepFake2017 -b -T ${SAMPLE_LIST}
SAMPLES=()
EXCLUDE=()
unset -f condor_submit
