import os

# Used to remove dummy "MakePlots.sh" files created after submitting jobs to condor

for x in range (0,19):

    os.remove('MakePlots' '%s' '.sh' % x)




