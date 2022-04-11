import sys,os,util,asyncio

def main():
    dataFile = sys.argv[1]
    logFile = dataFile+".log"
    real_command = await util.file_get_contents(dataFile)
    command = "{0} 1> '{1}' 2>&1".format(real_command,logFile)
    os.system(command)
    os.remove(dataFile)
    os.remove(logFile)
asyncio.run(main())