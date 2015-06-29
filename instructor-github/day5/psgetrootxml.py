__author__ = 'ravi'
import xml.etree.ElementTree as et
doc = et.parse('movies.xml')

root =  doc.getroot()
print root.tag
print root.attrib
print root.get('shelf')


