__author__ = 'ravi'

import xml.etree.ElementTree as et
xml_doc = et.parse('rootcap.xml')

root =  xml_doc.getroot()
print root[0].get('name')
print root[0][0].text
print root[-1].get('name')