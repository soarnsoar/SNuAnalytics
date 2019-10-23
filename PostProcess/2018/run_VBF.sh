SAMPLES=(
VBFHToWWToLNuQQ_M120
VBFHToWWToLNuQQ_M124
VBFHToWWToLNuQQ_M125
VBFHToWWToLNuQQ_M126
VBFHToWWToLNuQQ_M135
VBFHToWWToLNuQQ_M150
VBFHToWWToLNuQQ_M155
VBFHToWWToLNuQQ_M160
VBFHToWWToLNuQQ_M180
VBFHToWWToLNuQQ_M190
VBFHToWWToLNuQQ_M200
VBFHToWWToLNuQQ_M230
VBFHToWWToLNuQQ_M250
VBFHToWWToLNuQQ_M400
VBFHToWWToLNuQQ_M500
VBFHToWWToLNuQQ_M550
VBFHToWWToLNuQQ_M750
VBFHToWWToLNuQQ_M800
VBFHToWWToLNuQQ_M1500
VBFHToWWToLNuQQ_M4000
VBFHToWWToLNuQQ_M5000

)

#--Run--#

SAMPLE_LIST=''
EXCLUDE_LIST=''
for s in ${SAMPLES[@]};do SAMPLE_LIST=${s}','${SAMPLE_LIST};done
for e in ${EXCLUDE[@]};do EXCLUDE_LIST=${e}','${EXCLUDE_LIST};done


######################
# Option: -R(redo)
######################
#--l1Prod--#
#mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i Prod -s MCl1loose2018v5 -b -T ${SAMPLE_LIST} 
#--Corr--#
#mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5 -s MCCorr2018v5 -b -T ${SAMPLE_LIST}
#--Semilep--#
#mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5__MCCorr2018v5 -s Semilep2018 -b -T ${SAMPLE_LIST}
#--
mkPostProc.py -p Autumn18_102X_nAODv5_Full2018v5 -i MCl1loose2018v5__MCCorr2018v5__Semilep2018 -s HMlnjjSel2017 -b -T ${SAMPLE_LIST}