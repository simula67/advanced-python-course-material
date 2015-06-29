__author__ = 'antonjoj'

from os import stat, listdir
from os.path import isfile, isdir, join
from json import dump

def create_dict(directory_name):
    info = {}
    info[directory_name] = {}
    for file in [entry for entry in listdir(directory_name) if isfile(join(directory_name, entry))]:
        info[directory_name][file] = stat(join(directory_name, file)).st_size
    return info

info = create_dict('C:\\')

dump( info, open("tmp.json", "w"), indent=4)
# Similarly you have json load