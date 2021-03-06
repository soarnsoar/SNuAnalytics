# /xrootd//store/user/jhchoi/Latino/HWWNano/
# Sites_cfg: /xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/
# changed to /xrd/store/user/jhchoi/Latino/HWWNano/
# L1Loose


SAMPLES=(
VBFHToWWToLNuQQ_M200
VBFHToWWToLNuQQ_M230
VBFHToWWToLNuQQ_M250
VBFHToWWToLNuQQ_M270
VBFHToWWToLNuQQ_M300
VBFHToWWToLNuQQ_M350
VBFHToWWToLNuQQ_M400
VBFHToWWToLNuQQ_M450
VBFHToWWToLNuQQ_M500
VBFHToWWToLNuQQ_M550
VBFHToWWToLNuQQ_M600
VBFHToWWToLNuQQ_M650
VBFHToWWToLNuQQ_M700
VBFHToWWToLNuQQ_M750
VBFHToWWToLNuQQ_M800
VBFHToWWToLNuQQ_M1000
VBFHToWWToLNuQQ_M1500
VBFHToWWToLNuQQ_M2000
VBFHToWWToLNuQQ_M2500
VBFHToWWToLNuQQ_M4000
VBFHToWWToLNuQQ_M5000
)

EXCLUDE=()

#--Run--#
SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done
#echo ${SAMPLE_LIST}
#echo ${EXCLUDE_LIST}

######################
# Option: -R(redo)
######################


#--l1Prod--#
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i Prod -s MCl1loose2016v5 -b -T ${SAMPLE_LIST}
#--Corr--#
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5 -s MCCorr2016v5 -b -T ${SAMPLE_LIST}

#--semilep--#
mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5__MCCorr2016v5 -s Semilep2016 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5__MCCorr2016v5__Semilep2016 -s HMlnjjSel2017 -b -T ${SAMPLE_LIST}
#mkPostProc.py -p Summer16_102X_nAODv4_Full2016v5 -i MCl1loose2016v5__MCCorr2016v5__Semilep2016 -s HMlnjjSel_New -b -T ${SAMPLE_LIST}



SAMPLES=()
EXCLUDE=()
