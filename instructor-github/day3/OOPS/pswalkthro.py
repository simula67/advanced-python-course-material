__author__ = 'ravi'
from pprint import pprint
from os.path import walk, isfile


class WalkThrough(object):
    def visit(self, owt, directory_name, file_names):
        temp = filter(lambda fn: fn.endswith(self.file_selection),
                      file_names)
        self.content.append({directory_name: temp})

    def __init__(self, root_directory, file_selection):
        self.root_directory = root_directory
        self.file_selection = file_selection
        self.content = []
        self.__do_walk_through()

    def __do_walk_through(self):
        walk(self.root_directory, self.visit, None)


if __name__ == '__main__':
    wt = WalkThrough('/training/ravi/rootcap', '.pdf')
    pprint(wt.content)