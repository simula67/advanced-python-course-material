__author__ = 'ravi'

info = {'app': 'ws',
 'domain': 'rootcap.in',
 'hostname': 'ws100',
 'platform': 'linux4'}


print info['app']
print info['hostname']
print info.get('platform')
print info.get('platform12')
print info.get('platform12', 'unknown key')
