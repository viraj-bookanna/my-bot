import sys,os,time

dataFile = sys.argv[1]
logFile = dataFile+".log"
os.system("python sheller_helper.py {0} 1> {1} 2>&1".format(dataFile, logFile))
time.sleep(2)
os.remove(dataFile)
os.remove(logFile)
