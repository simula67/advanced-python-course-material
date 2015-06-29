__author__ = 'ravi'
"""
from xml.etree.ElementTree import ElementTree, Element, SubElement
from sys import stdout
root_tag = Element('directory')
root_tag.attrib['name'] = '/etc'

f1 = SubElement(root_tag, 'file')
f1.text = 'passwd'

f2 = SubElement(root_tag, 'file')
f2.text = 'group'

et = ElementTree(root_tag)
et.write('testit.xml')
"""
from shutil import move
from xml.etree.ElementTree import ElementTree, Element, SubElement
import xml.etree.ElementTree as et
doc = et.parse('testit.xml')
root_tag = doc.getroot()
f = SubElement(root_tag[0], 'file')
f.text = 'resolv.conf'
doc.write('testit2.xml')
move('testit2.xml', 'testit.xml')

