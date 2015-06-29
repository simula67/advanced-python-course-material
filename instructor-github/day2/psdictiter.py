__author__ = 'ravi'

info = {'app': 'ws',
 'domain': 'rootcap.in',
 'hostname': 'ws100',
 'platform': 'linux4'}

for key in info:
    print "{} : {}".format(key, info[key])

print

for key in sorted(info):
    print "{} : {}".format(key, info[key])

print

for key in sorted(info, key=lambda k: info[k]):
    print "{} : {}".format(key, info[key])



print


"""
print info.values()
print info.keys()
print info.items()
"""