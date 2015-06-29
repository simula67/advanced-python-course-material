import os

print "PID :  %d "  % os.getpid()
print 
p = os.fork()
print p
if p:
    print "parent"
    print "PID :  %d "  % os.getpid()
    print "PPID :  %d "  % os.getppid()
else:
    print "child"
    print "PID :  %d "  % os.getpid()
    print "PPID :  %d "  % os.getppid()
