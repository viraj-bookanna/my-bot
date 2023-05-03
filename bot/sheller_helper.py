import sys,os

def file_get_contents(fName):
    try:
        with open(fName, mode='r') as file:
            fdata = file.read()
        return fdata
    except:
        return ""
dataFile = sys.argv[1]
real_command = file_get_contents(dataFile)
os.system(real_command)
