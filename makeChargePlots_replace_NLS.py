import sys

import ROOT
from ROOT import *

# Script to make a single root file with QIE plots
# run like:
# python makeChargePlots_replace.py /hdfs/store/user/pintaric/DoubleMuon/crab_DoubleMuon__Run2018A-v1__RAW_315689/180525_122052/0000/HcalTupleMaker_314444_101.root /hdfs/store/user/pintaric/DoubleMuon/crab_DoubleMuon__Run2018A-v1__RAW_315689/180525_122052/0000/ /data/senka/HCAL/PFG/skims/DoubleMu/Run_315689/

# sys.argv is a list created by the command line.  Its a list of arguments that you attach to the Python command that opens the file.  

inputFileName = sys.argv[1]  # The first argument when opening the file will be the name of the file itself.
replaceThis = sys.argv[2] # The second argument will be 
replaceToThat = sys.argv[3]
NLS = int(sys.argv[4]) # The int function returns an integer object constructed from a number or string.  So based on argument 4 in the command line, it is converted from a string to integer.
#maxYbin = (sys.arg[5]) #max Ybin
print " reading in input file: ", inputFileName  # printed statements to the CL

output_path = "/home/kahn/CERN/CMSSW_9_0_0/src/HCALPFG/HcalTupleMaker/corrected_plots/"
output_name=replaceThis
output_name=output_path + output_name.replace(replaceThis,replaceToThat)  #Edits the input file name in order to create an output file name to which data from program can be added to
print " ==> output filename: ", output_name
file_output=ROOT.TFile(output_name,"recreate")  #Creates an output root file to store all the plots

#minmax = [float(sys.argv[1]),float(sys.argv[2])]
#parm = sys.argv[4]
file = TFile.Open(inputFileName,'READ') # opens the root file
file.cd('hcalTupleTree') # changing into the hcalTupleTree directory of the root file
limit = gDirectory.Get('tree')  # get data from the treer directory
#NEW CODE 
#Charge = gDirectory.Get('tree/QIE11DigiTotFC.QIE11DigiTotFC')

#Charge = limit.ls
#entries = limit.GetEntriesFast()
#print "This is Charge", Charge[5]
#print "This is Entries", entries 

nEntries = limit.GetEntries()-1 # Gets rid of the first null entry at the top of the vector

# 2D Histograms for QIE-HEM3 
histo_LS_HEM = TH2F('QIE_HEM3_Even_Phi','', 60,285.5,405.5,NLS,0,60000)  # arguments or creating histogram: 1. variable name for plot, 2. title of plot itself, 3. x dimension bin number (73 in case) 4. Starting X point 5. Enging X point 6. Y dimension bin number (NLS in this case). 7. Starting Y point 8. Ending y point.
limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:ls >> QIE_HEM3_Even_Phi", "(QIE11DigiIPhi.QIE11DigiIPhi ==8 || QIE11DigiIPhi.QIE11DigiIPhi ==10) && QIE11DigiIEta.QIE11DigiIEta < 0")
histo_LS_HEM.GetXaxis().SetTitle("Luminosity Section")
histo_LS_HEM.GetYaxis().SetTitle("QIE11-HEM03 Integrated Charge [fC]")
#histo_LS_HEM.GetXaxis().SetNdivisions(350)


histo_ch_HEM = TH2F('QIE_HEM3_Odd_Phi','', 60,285.5,405.5,NLS,0,60000)  # creating a 2nd histogram.
limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:ls >> QIE_HEM3_Odd_Phi", "(QIE11DigiIPhi.QIE11DigiIPhi == 7 || QIE11DigiIPhi.QIE11DigiIPhi == 9) && QIE11DigiIEta.QIE11DigiIEta < 0")   
histo_ch_HEM.GetXaxis().SetTitle("Luminosity Section")
histo_ch_HEM.GetYaxis().SetTitle("QIE11-HEM03 Integrated Charge [fC]")
#histo_LS_HEM.GetXaxis().SetNdivisions(350)



#histo_LS_HEP = TH2F('QIE_HEM3_vs_Even_Phi','', 3,7.5,10.5,NLS,0,2000) # Creating a 3rd histogram.
#limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:QIE11DigiIPhi.QIE11DigiIPhi >> QIE_HEM3_vs_Even_Phi","(QIE11DigiIPhi.QIE11DigiIPhi == 8 || QIE11DigiIPhi.QIE11DigiIPhi == 10) && QIE11DigiIEta.QIE11DigiIEta < 0")
#histo_LS_HEP.GetXaxis().SetTitle("#phi Sector")
#histo_LS_HEP.GetYaxis().SetTitle("QIE11-HEM03 Integrated Charge [fC]")

#histo_ch_HEP = TH2F('QIE_HEM3_vs_Odd_Phi','', 3,6.5,9.5,NLS,0,2000) # Creating a 4th histogram.
#limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:QIE11DigiIPhi.QIE11DigiIPhi >> QIE_HEM3_vs_Odd_Phi","(QIE11DigiIPhi.QIE11DigiIPhi == 7 || QIE11DigiIPhi.QIE11DigiIPhi == 9) && QIE11DigiIEta.QIE11DigiIEta < 0")
#histo_ch_HEP.GetXaxis().SetTitle("#phi Sector")
#histo_ch_HEP.GetYaxis().SetTitle("QIE11-HEM03 Integrated Charge [fC]")


#2D Histograms for QIE-HEM4
histo_LS_HEM2 = TH2F('QIE_HEM4_Even_Phi','', 60,285.5,405.5,NLS,0,60000)  # arguments or creating histogram: 1. variable name for plot, 2. title of plot itself, 3. x dimension bin number (73 in case) 4. Starting X point 5. Enging X point 6. Y dimension bin number (NLS in this case). 7. Starting Y point 8. Ending y point.
limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:ls >> QIE_HEM4_Even_Phi", "(QIE11DigiIPhi.QIE11DigiIPhi ==12 || QIE11DigiIPhi.QIE11DigiIPhi ==14) && QIE11DigiIEta.QIE11DigiIEta < 0")
histo_LS_HEM2.GetXaxis().SetTitle("Luminosity Section")
histo_LS_HEM2.GetYaxis().SetTitle("QIE11-HEM04 Integrated Charge [fC]")
#histo_LS_HEM2.GetXaxis().SetNdivisions(350)
histo_LS_HEM2.Draw("box")

histo_ch_HEM2 = TH2F('QIE_HEM4_Odd_Phi','', 60,285.5,405,NLS,0,60000)  # creating a 2nd histogram.
limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:ls >> QIE_HEM4_Odd_Phi", "(QIE11DigiIPhi.QIE11DigiIPhi == 11 || QIE11DigiIPhi.QIE11DigiIPhi == 13) && QIE11DigiIEta.QIE11DigiIEta < 0")   
histo_ch_HEM2.GetXaxis().SetTitle("Luminosity Section")
histo_ch_HEM2.GetYaxis().SetTitle("QIE11-HEM04 Integrated Charge [fC]")
#histo_LS_HEM2.GetXaxis().SetNdivisions(350)


#histo_LS_HEP2 = TH2F('QIE_HEM4_vs_Even_Phi','', 5,10.5,15.5,NLS,0,2000) # Creating a 3rd histogram.
#limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:QIE11DigiIPhi.QIE11DigiIPhi >> QIE_HEM4_vs_Even_Phi","(QIE11DigiIPhi.QIE11DigiIPhi == 12 || QIE11DigiIPhi.QIE11DigiIPhi == 14) && QIE11DigiIEta.QIE11DigiIEta < 0")
#histo_LS_HEP2.GetXaxis().SetTitle("#phi Sector")
#histo_LS_HEP2.GetYaxis().SetTitle("QIE11-HEM04 Integrated Charge [fC]")

#histo_ch_HEP2 = TH2F('QIE_HEM4_vs_Odd_Phi','', 5,9.5,14.5,NLS,0,2000) # Creating a 4th histogram.
#limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:QIE11DigiIPhi.QIE11DigiIPhi >> QIE_HEM4_vs_Odd_Phi","(QIE11DigiIPhi.QIE11DigiIPhi == 11 || QIE11DigiIPhi.QIE11DigiIPhi == 13) && QIE11DigiIEta.QIE11DigiIEta < 0")
#histo_ch_HEP2.GetXaxis().SetTitle("#phi Sector")
#histo_ch_HEP2.GetYaxis().SetTitle("QIE11-HEM04 Integrated Charge [fC]")

#canv2.cd()
#histo_LS_HEM.Draw("lego")
#canv2.SaveAs('histo_LS'+'_Run'+'.pdf')


#HEM3 Projections

#QIE_HEM3_EvenPhi_ProjX = histo_LS_HEM.ProjectionX("QIE_HEM3_EvenPhi_ProjX", 0, 126);
#QIE_HEM3_EvenPhi_ProjX.Draw();

#QIE_HEM3_EvenPhi_ProjY = histo_LS_HEM.ProjectionY("QIE_HEM3_EvenPhi_ProjY", 0, 2000);
#QIE_HEM3_EvenPhi_ProjY.Draw();

#QIE_HEM3_OddPhi_ProjX = histo_ch_HEM.ProjectionX("QIE_HEM3_OddPhi_ProjX", 0, 126);
#QIE_HEM3_OddPhi_ProjX.Draw();

#QIE_HEM3_OddPhi_ProjY = histo_ch_HEM.ProjectionY("QIE_HEM3_OddPhi_ProjY", 0, 2000);
#QIE_HEM3_OddPhi_ProjY.Draw();

#HEM4 Projections 

#QIE_HEM4_EvenPhi_ProjX = histo_LS_HEM2.ProjectionX("QIE_HEM4_EvenPhi_ProjX", 0, 126);
#QIE_HEM4_EvenPhi_ProjX.Draw();

#QIE_HEM4_EvenPhi_ProjY = histo_LS_HEM2.ProjectionX("QIE_HEM4_EvenPhi_ProjY", 0,2000);
#QIE_HEM4_EvenPhi_ProjY.Draw();

#QIE_HEM4_OddPhi_ProjX = histo_ch_HEM2.ProjectionX("QIE_HEM4_OddPhi_ProjX", 0, 126);
#QIE_HEM4_OddPhi_ProjX.Draw();

#QIE_HEM4_OddPhi_ProjY = histo_ch_HEM2.ProjectionX("QIE_HEM4_OddPhi_ProjY", 0, 2000);
#QIE_HEM4_OddPhi_ProjY.Draw();


#HEM3 2D Profiles 

histo_2LS_HEM = TProfile('QIE_HEM3_Even_Phi_Profile','', 60,285.5,405,0,60000)  # arguments or creating histogram: 1. variable name for plot, 2. title of plot itself, 3. x dimension bin number (73 in case) 4. Starting X point 5. Enging X point 6. Y dimension bin number (NLS in this case). 7. Starting Y point 8. Ending y point.
limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:ls >> QIE_HEM3_Even_Phi_Profile", "(QIE11DigiIPhi.QIE11DigiIPhi ==8 || QIE11DigiIPhi.QIE11DigiIPhi ==10) && QIE11DigiIEta.QIE11DigiIEta < 0")
histo_2LS_HEM.GetXaxis().SetTitle("Luminosity Section")
histo_2LS_HEM.GetYaxis().SetTitle("QIE11-HEM03 Integrated Charge [fC]")
#histo_2LS_HEM.GetXaxis().SetNdivisions(350)
#histo_2LS_HEM.Draw("box")

histo_2ch_HEM = TProfile('QIE_HEM3_Odd_Phi_Profile','', 60,285.5,405,0,60000)  # creating a 2nd histogram.
limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:ls >> QIE_HEM3_Odd_Phi_Profile", "(QIE11DigiIPhi.QIE11DigiIPhi == 7 || QIE11DigiIPhi.QIE11DigiIPhi == 9) && QIE11DigiIEta.QIE11DigiIEta < 0")   
histo_2ch_HEM.GetXaxis().SetTitle("Luminosity Section")
histo_2ch_HEM.GetYaxis().SetTitle("QIE11-HEM03 Integrated Charge [fC]")
#histo_2ch_HEM.GetXaxis().SetNdivisions(350)

#HEM4 2D Profiles 

histo_2LS_HEM2 = TProfile('QIE_HEM4_Even_Phi_Profile','', 60,285.5,405,0,60000)  # arguments or creating histogram: 1. variable name for plot, 2. title of plot itself, 3. x dimension bin number (73 in case) 4. Starting X point 5. Enging X point 6. Y dimension bin number (NLS in this case). 7. Starting Y point 8. Ending y point.
limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:ls >> QIE_HEM4_Even_Phi_Profile", "(QIE11DigiIPhi.QIE11DigiIPhi ==12 || QIE11DigiIPhi.QIE11DigiIPhi ==14) && QIE11DigiIEta.QIE11DigiIEta < 0")
gStyle.SetErrorX(0.);    
histo_2LS_HEM2.GetXaxis().SetTitle("Luminosity Section")
histo_2LS_HEM2.GetYaxis().SetTitle("QIE11-HEM04 Integrated Charge [fC]")
#histo_2LS_HEM2.GetXaxis().SetNdivisions(350)
#histo_2LS_HEM2.Draw("box")

histo_2ch_HEM2 = TProfile('QIE_HEM4_Odd_Phi_Profile','', 60,285.5,405,0,60000)  # creating a 2nd histogram.
limit.Draw("QIE11DigiTotFC.QIE11DigiTotFC:ls >> QIE_HEM4_Odd_Phi_Profile", "(QIE11DigiIPhi.QIE11DigiIPhi == 11 || QIE11DigiIPhi.QIE11DigiIPhi == 13) && QIE11DigiIEta.QIE11DigiIEta < 0")  
gStyle.SetErrorX(0.) 
histo_2ch_HEM2.GetXaxis().SetTitle("Luminosity Section")
histo_2ch_HEM2.GetYaxis().SetTitle("QIE11-HEM04 Integrated Charge [fC]")
#histo_2ch_HEM2.GetXaxis().SetNdivisions(350)

#Overlay of 2D Proiles for HEM3 and HEM4

#c2 = TCanvas("c2", "", 800, 800) 
#prof1 = histo_2LS_HEM.Get("QIE_HEM3_Even_Phi_Profile") 
#prof2 = histo_2LS_HEM2.Get("QIE_HEM4_Even_Phi_Profile")

#prof1.SetLineColor(4)
#prof2.SetLineColoe(8)

#prof1.Draw()
#prof2.Draw("same")
#c2.Update()


file_output.cd()  # Change into the output root file. 

#Writing 2D Histograms to File
histo_LS_HEM.Write('QIE_HEM3_Even_Phi') # Write to the output file
histo_ch_HEM.Write('QIE_HEM3_Odd_Phi')
#histo_LS_HEP.Write('QIE_HEM3_vs_Even_Phi')
#histo_ch_HEP.Write('QIE_HEM3_vs_Odd_Phi')
histo_LS_HEM2.Write('QIE_HEM4_Even_Phi') # Write to the output file
histo_ch_HEM2.Write('QIE_HEM4_Odd_Phi')
#histo_LS_HEP2.Write('QIE_HEM4_vs_Even_Phi')
#histo_ch_HEP2.Write('QIE_HEM4_vs_Odd_Phi')

#Writing X-Y Projections to File
#QIE_HEM3_EvenPhi_ProjX.Write('QIE_HEM3_EvenPhi_ProjX')
#QIE_HEM3_EvenPhi_ProjY.Write('QIE_HEM3_EvenPhi_ProjY')

#QIE_HEM3_OddPhi_ProjX.Write('QIE_HEM3_OddPhi_ProjX')
#QIE_HEM3_OddPhi_ProjY.Write('QIE_HEM3_OddPhi_ProjY')

#QIE_HEM4_EvenPhi_ProjX.Write('QIE_HEM4_EvenPhi_ProjX')
#QIE_HEM4_EvenPhi_ProjY.Write('QIE_HEM4_EvenPhi_ProjY')

#QIE_HEM4_OddPhi_ProjX.Write('QIE_HEM4_OddPhi_ProjX')
#QIE_HEM4_OddPhi_ProjY.Write('QIE_HEM4_OddPhi_ProjY')

#Writing 2-D Profiles to File

histo_2LS_HEM.Write('QIE_HEM3_Even_Phi_Profile')
histo_2ch_HEM.Write('QIE_HEM3_Odd_Phi_Profile')

histo_2LS_HEM2.Write('QIE_HEM4_Even_Phi_Profile')
histo_2ch_HEM2.Write('QIE_HEM4_Odd_Phi_Profile')

#c2.SaveAs("TestOverlay.png")


