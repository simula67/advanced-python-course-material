# Import the FTP object from ftplib
from ftplib import FTP
from getpass import getpass
import os

    

ftp = FTP('localhost')

print 'Welcome to 16.154.161.14'
print 'Logging in.'
print ftp.login('ravi', getpass('Enter the password :'))

ftp.retrlines('LIST')

#print 'Closing FTP connection'
print ftp.close()
