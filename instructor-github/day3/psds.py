__author__ = 'ravi'

info = {'name': 'cameron',
        'occupation': ['writer', 'directory', 'prod'],
        'interest': {'read': ['sci-fi', 'fiction'],
                     'others': ['cook', 'swim']},
        'place': 'hollywood'}

for tags in info:
    if type(info[tags]) is list:
        print tags
        for occupation in info[tags]:
            print "\t", occupation
    else:
        print "{} :{}".format(tags, info[tags])
