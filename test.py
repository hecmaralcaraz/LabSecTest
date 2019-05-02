import subprocess


python3 --version

x = subprocess.getstatusoutput('')

if x[0] > 0:
    print('mal')
elif x[0] == 0:
    print('bien')