__author__ = 'antonjoj'
import xml.etree.ElementTree as et

doc = et.parse("movies.xml")
for movie in doc.iter('movie'):
    print "{} : {} ".format(movie.tag, movie.get('title'))
    for movie_info in movie:
        print "\t{} {}".format(movie_info.tag, movie_info.text)