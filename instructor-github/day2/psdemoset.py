__author__ = 'ravi'
from pprint import  pprint

def get_user_without_grp(passwd, group):
    users = {l.split(':')[0] for l in open(passwd)}
    groups = {l.split(':')[0] for l in open(group)}
    return users - groups

def get_user_with_grp(passwd, group):
    users = {l.split(':')[0] for l in open(passwd)}
    groups = {l.split(':')[0] for l in open(group)}
    return users & groups

uwg = get_user_without_grp(r'/etc/passwd', r'/etc/group')
pprint(list(uwg))

