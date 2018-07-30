#!/usr/bin/python
#used to submit multiple jobs to condor
import os, sys
import shlex, subprocess
from datetime import datetime, date, time
from time import sleep
import shutil
import numpy as np   
#sys.path.append(os.path.abspath(os.path.curdir))

JobTime = datetime.now()
fTag = JobTime.strftime("%Y%m%d_%H%M%S")
sTag = "PFG"
dirname = "jobs/%s_%s"%(sTag,fTag)
#DetType = "1" #rod
logFile = "0730.log"

try:
    os.makedirs(dirname)
except:
    pass

ProdTag = "Run1_20180730"
OutDir  = "/home/kahn/CERN/CMSSW_9_0_0/src/HCALPFG/HcalTupleMaker/condor_out"
WorkDir = "/home/kahn/CERN/CMSSW_9_0_0/src/HCALPFG/HcalTupleMaker"

try:
    os.makedirs(OutDir)
except:
    pass

try:
    os.makedirs(OutDir+"/"+ProdTag)
except:
    pass

try:    os.makedirs(OutDir+"/"+ProdTag+"/logs")
except:
    pass



#########################################
#make sure OutDir is the same in main.cc
#########################################
condor_script_template = """
universe = vanilla
Executable = ./MakePlots.sh
+IsLocalJob = true
Should_transfer_files = NO
Requirements = TARGET.FileSystemDomain == "privnet"
Output = %(OUTDIR)s/%(MYPREFIX)s/logs/%(FILENAME)s_sce_$(cluster)_$(process).stdout
Error  = %(OUTDIR)s/%(MYPREFIX)s/logs/%(FILENAME)s_sce_$(cluster)_$(process).stderr
Log    = %(OUTDIR)s/%(MYPREFIX)s/logs/%(FILENAME)s_sce_$(cluster)_$(process).condor
Arguments = %(VERSION)s
Queue 1
 
"""
##########################################



#################################

#range to loop over
Arr = [21, 22, 23, 24, 25, 26, 27, 28]
IN = 21
version = 21
#maxYbins = [5, 5, 5, 5, 5, 5]
#INBIN = 5
#maxYbin = 5
#pauser = 1;
for q in range(0,len(Arr)):
#for q in range(0,len(Arr)):
    version = Arr[q]
    #if (pauser % 30 == 0):
    #    sleep(3600);

    #pauser = pauser + 1; 
    # Creating new file                                                              
    shutil.copy2('MakePlots.sh', 'MakePlots' '%s' '.sh' % q)

    # Reading in the file                                                            
    with open('MakePlots' '%s' '.sh' % q, 'r') as file :
        filedata = file.read()

    # Replacing the target string
        
        j = "_" + str(Arr[q])
    #i = str(Initial)
        i = "_" + str(IN)
    
 #       b = "sdewfd" + str(maxybins[q])
  #      a = "sdfdew" + str(INBIN)
        filedata = filedata.replace(i, j)
   #     filedata = filedata.replace(a, b)
        

    # Writing out the new file                                                       
    with open('MakePlots' '%s' '.sh' % q, 'w') as file:
        file.write(filedata)

    # Defining the infile                                                            
    InFile = 'MakePlots' '%s' '.sh' % q

 
    kw = {}

    kw["MYPREFIX"]  = ProdTag
#kw["WORKDIR"]   = WorkDir
    kw["OUTDIR"]    = OutDir
    kw["INPUT"]     = InFile
    kw["FILENAME"]  = sTag
    kw["VERSION"]   = version
    #kw["MAXYBIN"]   = maxYbin
#kw["DETTYPE"]   = DetType
#kw["LOGFILE"]   = logFile

    script_str = condor_script_template % kw
    f = open("%s/condor_jobs_%s_G4Sim.jdl"%(dirname,sTag), 'w')
    f.write(script_str)
    f.close()

    condorcmd = "condor_submit %s/condor_jobs_%s_G4Sim.jdl"%(dirname,sTag)
    print 'condorcmd: ', condorcmd
    print ('Executing condorcmd')

    p=subprocess.Popen(condorcmd, shell=True)
    p.wait()
   
    
    print "\n"
    #print "Histos output dir: %s/%s"%(OutDir,ProdTag)

#print(Arr)
