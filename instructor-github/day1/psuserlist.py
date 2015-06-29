__author__ = 'ravi'

def get_users_list(file_name):
    users_list = []

    with open(file_name) as fp:
        for line in fp:
            users_list.append(line.split(':')[0].title())

    with open('userlist.dat', 'w') as fw:
        for ln, login in enumerate(sorted(users_list), 1):
            content = "{:>6}  {}".format(ln, login)
            fw.write(content + "\n")
            print content

get_users_list('/etc/passwd')