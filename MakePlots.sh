#!/bin/bash

#Exectuable called by the condor script "submitjobs.py"

VERSION=$1
#MAXYBIN=$2
echo $VERSION
# setup CMSSW software environment at UMD
export VO_CMS_SW_DIR=/sharesoft/cmssw
. $VO_CMS_SW_DIR/cmsset_default.sh
cd //home/kahn/CERN/CMSSW_9_0_0/src/HCALPFG/HcalTupleMaker

eval `scramv1 runtime -sh`


if [[ "$VERSION" -eq 21 ]]; then
    python makeChargePlots_replace_NLS.py /store/user/abkahn/317340/try15/ZeroBias/crab_ZeroBias__Run2018B-v1__Run_317340_try15/180725_212824/0000/HcalTupleMaker_317340_21.root HcalTupleMaker_317340_21 QIE\
plot_21.root 300

elif [[ "$VERSION" -eq 22 ]]; then
    python makeChargePlots_replace_NLS.py /store/user/abkahn/317340/try15/ZeroBias/crab_ZeroBias__Run2018B-v1__Run_317340_try15/180725_212824/0000/HcalTupleMaker_317340_22.root HcalTupleMaker_317340_22 QIE\
plot_22.root 300


elif [[ "$VERSION" -eq 23 ]]; then
    python makeChargePlots_replace_NLS.py /store/user/abkahn/317340/try15/ZeroBias/crab_ZeroBias__Run2018B-v1__Run_317340_try15/180725_212824/0000/HcalTupleMaker_317340_23.root HcalTupleMaker_317340_23 QIE\
plot_23.root 300


elif [[ "$VERSION" -eq 24 ]]; then
    python makeChargePlots_replace_NLS.py /store/user/abkahn/317340/try15/ZeroBias/crab_ZeroBias__Run2018B-v1__Run_317340_try15/180725_212824/0000/HcalTupleMaker_317340_24.root HcalTupleMaker_317340_24 QIE\
plot_24.root 300


elif [[ "$VERSION" -eq 25 ]]; then
    python makeChargePlots_replace_NLS.py /store/user/abkahn/317340/try15/ZeroBias/crab_ZeroBias__Run2018B-v1__Run_317340_try15/180725_212824/0000/HcalTupleMaker_317340_25.root HcalTupleMaker_317340_25 QIE\
plot_25.root 300


elif [[ "$VERSION" -eq 26 ]]; then
    python makeChargePlots_replace_NLS.py /store/user/abkahn/317340/try15/ZeroBias/crab_ZeroBias__Run2018B-v1__Run_317340_try15/180725_212824/0000/HcalTupleMaker_317340_26.root HcalTupleMaker_317340_26 QIE\
plot_26.root 300


elif [[ "$VERSION" -eq 27 ]]; then
    python makeChargePlots_replace_NLS.py /store/user/abkahn/317340/try15/ZeroBias/crab_ZeroBias__Run2018B-v1__Run_317340_try15/180725_212824/0000/HcalTupleMaker_317340_27.root HcalTupleMaker_317340_27 QIE\
plot_27.root 300


elif [[ "$VERSION" -eq 28 ]]; then
    python makeChargePlots_replace_NLS.py /store/user/abkahn/317340/try15/ZeroBias/crab_ZeroBias__Run2018B-v1__Run_317340_try15/180725_212824/0000/HcalTupleMaker_317340_28.root HcalTupleMaker_317340_28 QIE\
plot_28.root 300


else
    echo "Invalid Lumi Section Range"
fi
