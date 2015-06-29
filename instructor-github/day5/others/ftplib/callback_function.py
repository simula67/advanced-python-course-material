>>> def handle(data):
...      print data
... 
>>> def getdata(a, b, fun_name):
...      fun_name(str(a) + str(b))
... 
>>> getdata(100, 12.12, handle)
10012.12
>>> 

