__author__ = 'ravi'
from os.path import walk
from json import dump

def load_directory_content(o_dwt, dirname, file_names):

        selected_files = filter(lambda fn: fn.endswith(o_dwt.selector),
                                 file_names)
        if selected_files:
            o_dwt.content.append({dirname: selected_files})

class DirectoryWalkThrough(object):
    def __init__(self, root_path, selector):
        self.root_path = root_path
        self.selector = selector
        self.content = []
        self.do_load_content()

    def do_load_content(self):
        walk(self.root_path, load_directory_content, self)

    def to_json(self, json_file):
        dump(self.content, open(json_file, 'w'), indent=4)



if __name__ == '__main__':
    e = DirectoryWalkThrough('/home/ravi/rootcap', 'pdf')
    e.to_json('rootcap.json')
    """
    from pprint import pprint
    pprint(e.content)
    """