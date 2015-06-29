__author__ = 'ravi'
from xml.etree.ElementTree import ElementTree, Element, SubElement
from sys import stdout

root_tag = Element('directories')

directory_tag = SubElement(root_tag, 'directory')
directory_tag.attrib['name'] = '/home/ravi'

file_tag1 = SubElement(directory_tag, 'file')
file_tag1.text = 'sample.pdf'

et = ElementTree(root_tag)
et.write('test.xml')
