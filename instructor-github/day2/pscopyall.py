__author__ = 'ravi'
from sys import argv

def copy_all(*files):
    if len(files) < 3:
        raise RuntimeError("insuf. args")

    with open(files[-1], 'w') as fw:
        for file_name in files[:-1]:
            fw.write(file_name.center(60, '-')+"\n")
            fw.write(open(file_name).read())
            fw.write('-'.center(60, '-')+"\n")
try:
    copy_all(*argv[1:])
except RuntimeError, e:
    print e
