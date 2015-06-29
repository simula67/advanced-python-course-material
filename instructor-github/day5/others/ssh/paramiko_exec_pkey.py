#!/usr/bin/env python

import paramiko

hostname = 'ravijaya.info'
port = 22
username = 'ravijaya'
pkey_file = '/home/ravi/.ssh/id_rsa'

if __name__ == "__main__":
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, pkey=key)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print stdout.read()
    s.close()
