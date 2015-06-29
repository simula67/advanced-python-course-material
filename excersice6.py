__author__ = 'antonjoj'

from pprint import pprint

#occurance of words

occurence = {}

for line in open("datafiles\\passwd"):
    for word in line.rstrip().split(" "):
        occurence[word] = occurence.get( word, 0) + 1
pprint(occurence)