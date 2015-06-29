__author__ = 'ravi'
import subprocess
content = ''

cat = subprocess.Popen('cat /etc/resolv.conf',
                      stdout=subprocess.PIPE, shell=True)

tr = subprocess.Popen('python tr.py', stdout=subprocess.PIPE,
                      stdin=cat.stdout, shell=True)

for temp in tr.communicate():
    if temp:
        content += temp
print content

