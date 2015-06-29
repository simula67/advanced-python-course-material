__author__ = 'ravi'
from xml.etree.ElementTree import ElementTree, Element, SubElement
from sys import argv
import json
from pprint import pprint

class JSON2XML(object):
    def __init__(self, json_file, xml_file):
        self.json_file = json_file
        self.xml_file = xml_file
        self.content = None
        self.load_json()
        self.write_xml()

    def load_json(self):
        self.content = json.load(open(self.json_file))

    def write_xml(self):
        directory_name = self.content.keys()[0]
        root_tag = Element('directory')
        root_tag.attrib['name'] = directory_name

        files_tag = SubElement(root_tag, 'files')

        for file_name in self.content[directory_name]:
            file_tag = SubElement(files_tag, 'file')
            file_tag.attrib['size'] = \
                str(self.content[directory_name][file_name])
            file_tag.text = file_name

        ElementTree(root_tag).write(self.xml_file)


def main():
    xml = JSON2XML(argv[1], argv[2])

if __name__ == '__main__':
    main()










