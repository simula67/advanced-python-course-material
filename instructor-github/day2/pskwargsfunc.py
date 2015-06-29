__author__ = 'ravi'

def demo(**args):
    print args

demo()
demo(hostname='ws1', application="ws", platform='linux2')

info = {'version': 2.2, 'application': 'ws', 'hostname':
    'ws1', 'platform': 'linux2'}

demo(**info)


