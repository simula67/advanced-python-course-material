__author__ = 'antonjoj'

# Give me an ordered list of local users

usernames = []
with open("datafiles\\passwd") as fp:
    for line in fp:
        usernames.append(line.split(":")[0])
usernames.sort()
with open("userlist.txt", "w") as fw:
    for index, username in enumerate(usernames,1):
        content = "{:>6} {}".format(index, username.upper())
        fw.write(content + '\n')
        print content
