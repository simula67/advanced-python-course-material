__author__ = 'ravi'
from pprint import pprint

info = {'app': 'ws',
 'domain': 'rootcap.in',
 'hostname': 'ws100',
 'platform': 'linux4'}

value = info.pop('hostname')
print value; print

del info['domain']

pprint(info)

