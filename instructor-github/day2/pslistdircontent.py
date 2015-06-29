__author__ = 'ravi'
from json import dump
from os import stat, listdir
from os.path import join, isfile
from  pprint import pprint


def get_file_size(directory_name):
    content = {}

    for file_name in listdir(directory_name):
        abs_path = join(directory_name, file_name)
        if isfile(abs_path):
            content.setdefault(directory_name, {})[file_name] = \
                stat(abs_path).st_size
    return content

dir_info = get_file_size('/tmp')
dump(dir_info, open('tmp.json', 'w'), indent=4)
