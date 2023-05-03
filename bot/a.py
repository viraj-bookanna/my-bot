import os,subprocess,sys

subprocess.Popen("python sheller.py a.txt".split(), shell=False, stdin=None, stdout=None, stderr=None, close_fds=True, creationflags=0x00000008,)
for i in range(40):
    print(i)