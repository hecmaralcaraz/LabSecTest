import subprocess

print (subprocess.getstatusoutput('zenityy --version'))
print('--> Python >= 3', subprocess.getstatusoutput('python3 --version'))
