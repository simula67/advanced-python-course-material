__author__ = 'ravi'
from pprint import pprint

def get_word_count(file_name):
    content = {}

    for line in open(file_name):
        for word in line.rstrip().split(' '):
            content[word] = content.get(word, 0) + 1

    return content

words = get_word_count('mesg')
pprint(words)
