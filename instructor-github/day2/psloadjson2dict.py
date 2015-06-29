__author__ = 'ravi'
from json import load

content = load(open('tmp.json'))

for directory_name in content:
    print directory_name
    for file_name in content[directory_name]:
        print "\t{} : {}".format(file_name,
                                 content[directory_name][file_name] )

