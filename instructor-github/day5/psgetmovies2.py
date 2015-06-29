__author__ = 'ravi'
import xml.etree.ElementTree as et
doc = et.parse('movies.xml')
root = doc.getroot()

print root[-1][-1].tag
print root[-1][-1].text
