__author__ = 'ravi'
\
import xml.etree.ElementTree as et
doc = et.parse('movies.xml')

for movie_tag in doc.iterfind('movie'):
    print movie_tag.get('title')
    print "\t{} : {}".format(movie_tag[-2].tag, movie_tag[-2].text)
    print "\t{} : {}".format(movie_tag[-1].tag, movie_tag[-1].text)
    print 
