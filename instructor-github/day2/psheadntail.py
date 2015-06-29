__author__ = 'ravi'
from collections import deque

def headntail(file_name, **param):
    count = param.get('count', 10)
    order = param.get('order', 'head')
    temp = ""
    line_counter = 1
    with open(file_name) as fp:
        if order == 'head':
            for line in fp:
                temp += line
                line_counter += 1
                if line_counter > count:
                    break
            return temp
        elif order == 'tail':
            temp = deque(fp, count)

    return ''.join(temp)

print headntail('/etc/passwd', order='tail', count=4)


"""
headntail('/etc/passwd', count=4)  #head  -4 /etc/passwd
headntail('/etc/passwd', count=14, order='tail') #tail  -14 /etc/passwd
headntail('/etc/passwd', count=1, order='head') #head  -1 /etc/passwd
"""