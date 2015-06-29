__author__ = 'ravi'
from xml.etree.ElementTree import ElementTree, Element, SubElement
import sys

root = Element('directory')
root.attrib['name'] = '/tmp'

files = SubElement(root, 'files')
file1 = SubElement(files, 'file')
file1.attrib['size'] = "1234"
file1.text = 'file1.txt'

et = ElementTree(root)
et.write('dummy.xml')


