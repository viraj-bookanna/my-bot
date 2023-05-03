import time,os,sys

time.sleep(1)
os.system("echo ses")
time.sleep(5)
os.system("echo ses2")
time.sleep(1)
print("This is standard error",file=sys.stderr)
time.sleep(10)