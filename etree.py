__author__ = 'antonjoj'
from xml.etree.ElementTree import  ElementTree, Element, SubElement
root_tag = Element("directory")
root_tag.attrib['name'] = '/etc'

f1 = SubElement(root_tag, 'file')
f1.text = 'passwd'

f2 = SubElement(root_tag, 'file')
f2.text = 'group'

et = ElementTree(root_tag)
et.write('testit.xml')