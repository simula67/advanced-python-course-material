__author__ = 'antonjoj'


def demo(**args):
    #args is dict
    print args

demo()
demo( hostname="ws1", application="hi")

info = {"version" : 2.2, "application": "ws"}
demo(**info)