# HcalTupleMaker
EDM analyzer for making ntuples from HCAL DIGIs and RecHits

## To build
```
# setup environment  
export SCRAM_ARCH=slc6_amd64_gcc530  

# setup cmssw release  
cmsrel CMSSW_9_0_0  
cd CMSSW_9_0_0/src  
cmsenv    

# clone repository  
mkdir HCALPFG  
cd HCALPFG  
git clone -b PFG-CMSSW_9_0_X  git@github.com:HCALPFG/HcalTupleMaker.git  

# compile code  
cd HcalTupleMaker  
scram b -j 8
```

## To run
```
# setup cmssw environment  
cd HCALPFG/HcalTupleMaker/test  
cmsenv  

# obtain grid proxy (optional)  
voms-proxy-init -voms cms -rfc  

# local runs  
cmsRun pfg_Local_RAW_cfg.py

# global runs  
cmsRun pfg_Global_RAW_cfg.py
```
## To Create Ntuples and Generate Plots
Overall Process for using crab and condor to generate Ntuples:
1. Run crab_submit (it’s connected with pfg_QIE11_Global_RAW_noSkim_cfg_crab.py and both are in the /test directory) to generate and then store the Ntuples in the UMD cluster
2. Got to the umd cluster and run submit jobs (which runs MakePlots.sh which runs makeChargePlots_replace_NLS.py multiple times) outputting the root files in a folder specified in makeChargePlots_replace_NLS.py.
3. Use hadd.py to merge into one root file, then use beautifier to clean up.

## Local runs

1. Local runs can be found on the HCAL DPG eos space  
    * /eos/cms/store/group/dpg_hcal/comm_hcal/USC/runXXXXXX/USC_XXXXXX.root

2. Access this space using the `root://eoscms.cern.ch/` redirector  
    * root://eoscms.cern.ch//eos/cms/store/group/dpg_hcal/comm_hcal/USC/runXXXXXX/USC_XXXXXX.root

3. If you wish to browse this space, do an `eosmount` on lxplus

4. Copy a file locally using `xrdcp`

## Global runs

1. Choose the correct global tag  
    * https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions

2. Run information:  
    * https://cmswbm.cern.ch/

---------------
Maintained by HCAL PFG  
Original author: Edmund Berry <Edmund.A.Berry(at)CERN.CH>
