__author__ = 'antonjoj'

from os.path import walk, isfile, join
from pprint import pprint

def visit(owt, directory_name, filenames):
    temp = filter(lambda fn: fn.endswith(owt.file_selection) and isfile(join(directory_name,fn)), filenames)
    if temp:
        owt.content.append({directory_name : temp})


class WalkThrough(object):
    def __init__(self, root_directory, file_selection):
        self.root_directory = root_directory
        self.file_selection = file_selection
        self.content = []
        self.__do_walk_through()

    def __do_walk_through(self):
        walk(self.root_directory, visit, self)



if __name__ == '__main__':
    wt = WalkThrough("C:\\Users\\antonjoj", "pdf")
    pprint(wt.content)