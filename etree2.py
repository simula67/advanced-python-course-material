__author__ = 'antonjoj'

from shutil import move

from xml.etree.ElementTree import SubElement
import xml.etree.ElementTree as et

doc = et.parse("testit.xml")
root_tag = doc.getroot()
f = SubElement(root_tag, 'file')
f.text = 'resolv.conf'
doc.write('testit2.xml')
move('testit2.xml', 'testit.xml')
