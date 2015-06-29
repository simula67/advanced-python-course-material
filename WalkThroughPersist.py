__author__ = 'antonjoj'

from excersice14 import WalkThrough
from json import dump
import pickle

class WalkThroughPersist(WalkThrough):
    def __init__(self, directory_name,file_selection, **param):
        super(WalkThroughPersist, self).__init__(directory_name,file_selection)
        self.type = param.get("type", "json")
        self.filename = param.get("filename", "temp")
        self.serialize()

    def serialize(self):
        if(self.type == "json"):
            dump(self.content, open(self.filename, "w"))
        elif(self.type == "python"):
            pickle.dump(self.content, open(self.filename, "w"))


if __name__ == '__main__':
    WalkThroughPersist("C:\\Users\\antonjoj", "pdf" , type="json", filename="antonjojpdf.json")