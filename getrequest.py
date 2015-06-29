__author__ = 'antonjoj'

import requests
import tempfile
import fileinput
import threading

from collections import deque

proxies = {
    "http": "http://proxy.ind.hp.com:8080",
    "https": "http://proxy.ind.hp.com:8080",
    }

def make_request(url, temp_file, lock):
    r = requests.get(url, proxies=proxies)
    if r.status_code == 200:
        open(temp_file, "w").write(r.text)
    else:
        print "FAILED : {}".format(r)
    with lock:
        print "URL : {}".format(url)
        for line in deque(open(temp_file), maxlen=5):
            print line

for host_url in fileinput.input():
    lock = threading.Lock()
    host_url = host_url.rstrip()
    t = threading.Thread(target=make_request, args=("http://{}/".format(host_url), tempfile.mktemp(), lock))
    t.start()

for t in threading.enumerate():
    if t is not threading.currentThread():
        t.join()

print "End of main thread"