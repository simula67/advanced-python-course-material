__author__ = 'ravi'
import subprocess
#subprocess.check_call('ls', shell=True)

d = subprocess.Popen('dir ..', shell=True, stdout=subprocess.PIPE)

content = ''
for temp in d.communicate():
    if temp:
        content += temp

print content

"""
op = subprocess.check_output('dir /etc', shell=True)
print op
"""
