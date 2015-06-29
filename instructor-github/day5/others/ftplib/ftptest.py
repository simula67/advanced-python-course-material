# Import the FTP object from ftplib
from ftplib import FTP
from getpass import getpass
import os

def handleDownload(block):
    fp.write(block)
    print ".",
    
ftp = FTP('16.154.161.39')

print 'Welcome to 16.154.161.39'
print 'Logging in.'
print ftp.login('ravi', getpass('Enter the password :'))

filename = 'passwd'

os.chdir('/tmp')
# Open the file for writing in binary mode
print 'Opening local file ' + filename
fp = open(filename, 'wb')

print 'Getting ' + filename
ftp.retrbinary('RETR ' + filename, handleDownload)

# Clean up time
print 'Closing file ' + filename
fp.close()

print 'Closing FTP connection'
print ftp.close()
