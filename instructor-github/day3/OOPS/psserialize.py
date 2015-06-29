__author__ = 'ravi'
from pswalkthro import WalkThrough
from json import dump
import pickle

class WalkThrough2Persist(WalkThrough):
    def __init__(self, directory_name, file_selection, **param):
        super(WalkThrough2Persist, self).__init__(directory_name,
                                                  file_selection)
        self.type = param.get('type', 'python')
        self.filename = param.get('filename', 'temp')
        self.to_serialize()

    def to_serialize(self):
        if self.type == 'python':
            pickle.dump(self.content, open(self.filename, "w"))
        elif self.type == 'json':
            dump(self.content, open(self.filename, "w"), indent=4)


if __name__ == '__main__':
    WalkThrough2Persist('/training/ravi/rootcap', '.pdf',
                        type='python', filename='rootcap.pick')



