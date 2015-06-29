__author__ = 'ravi'

import xml.etree.ElementTree as et
doc = et.parse('movies.xml')

for movie_tag in doc.iterfind('movie'):
    print movie_tag.get('title')
    for movie_info in movie_tag:

        print "\t{} : {}".format(movie_info.tag, movie_info.text)
    print
