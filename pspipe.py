__author__ = 'antonjoj'

import subprocess


cat = subprocess.Popen('type datafiles\\passwd', shell=True, stdout=subprocess.PIPE)
find = subprocess.Popen('find \"root\"', stdout=subprocess.PIPE, shell=True, stdin=cat.stdout)

for line in find.communicate():
    if line:
        print line