__author__ = 'ravi'
import xml.etree.ElementTree as et
doc = et.parse('movies.xml')

for movie in doc.iter('movie'):
    print "{} : {}".format(movie.tag, movie.get('title'))
    for mov_info in movie:
        print "\t{}: {}".format(mov_info.tag, mov_info.text)

    print

