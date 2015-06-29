__author__ = 'antonjoj'

users = {line.split(":")[0] for line in open("datafiles\\passwd")}
groups = {line.split(":")[0] for line in open("datafiles\\group")}

print "Users with groups :"
print users & groups

print "Users without groups :"
print users | groups

print "Groups without users"
print groups - users