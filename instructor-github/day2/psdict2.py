__author__ = 'ravi'
from pprint import pprint

info = {'hostname': 'ws1', 'domain': 'rootcap.in', 'platform': 'linux4'}

info['app'] = 'ws'

key = 'hostname'

if key in info:
    info[key] = 'ws100'

pprint(info)

