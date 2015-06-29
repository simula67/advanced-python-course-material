__author__ = 'ravi'
from json import load
from xml.etree.ElementTree import ElementTree, Element, SubElement

class JSON2XML(object):
    def __init__(self, json_file, xml_file):
        self.json_file = json_file
        self.xml_file = xml_file
        self.write_xml()

    def write_xml(self):
        content = load(file(self.json_file))
        root_tag = Element('directories')
        for directory in content:
            for directory_name in directory:
                dir_tag = SubElement(root_tag, 'directory',
                                     attrib={'name': directory_name})
                for file_name in directory[directory_name]:
                    file_tag = SubElement(dir_tag, 'file')
                    file_tag.text = file_name

        ElementTree(root_tag).write(self.xml_file)

if __name__ == '__main__':
    JSON2XML('rootcap.json', 'rootcap.xml')