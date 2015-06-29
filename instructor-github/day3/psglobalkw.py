__author__ = 'ravi'
counter = 0

def call_counter():
    global counter
    counter += 1

call_counter()
call_counter()
call_counter()

print counter
print __name__
