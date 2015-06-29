__author__ = 'ravi'

import xml.etree.ElementTree as et
doc = et.parse('rootcap.xml')

doc.getroot().remove(doc.getroot()[0])
doc.write('changed.xml')

#for d_tag in  doc.iter('file'):
#    print d_tag.text