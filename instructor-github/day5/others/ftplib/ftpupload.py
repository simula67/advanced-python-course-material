#!/usr/bin/env python

import ftplib
import os
from getpass import getpass

def upload(ftp, file):
    #ftp.cwd('/downloads/python/hp/nov-17-21-2014/')
    ftp.storlines("STOR " + file, open(file))

ftp = ftplib.FTP("localhost")
ftp.login("ravi", getpass("Enter the password: "))
os.chdir('/etc/')
upload(ftp, "resolv.conf")
