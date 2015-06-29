#!/usr/bin/env python
from getpass import getpass
import paramiko

hostname = 'localhost'
port = 22
username = 'ravi'
password = getpass()

if __name__ == "__main__":
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('whoami')
    print stdout.read()
    #help(s.invoke_shell)
    #print s.invoke_shell()
    #from time import sleep
    #sleep(13)
   # s.close()
