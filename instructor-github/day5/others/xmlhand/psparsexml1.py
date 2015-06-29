__author__ = 'ravi'

import xml.etree.ElementTree as et
doc = et.parse('movies.xml')
root_tag = doc.getroot()

print root_tag.tag
print root_tag.get('shelf')

