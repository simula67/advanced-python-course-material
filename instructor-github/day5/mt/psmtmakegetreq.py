import requests
import tempfile
import fileinput
import logging
import threading

proxy_setup = {'http': "http://web-proxy.ind.hp.com:8080/",
               'https': "http://web-proxy.ind.hp.com:8080/"}

fmt= "%(threadName)s %(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)

def make_request(url, temp_file):
    try:
        logging.debug("{}: {}".format(url, temp_file))
        r = requests.get(url,
                         proxies=proxy_setup)
        if r.status_code == 200:
            open(temp_file, 'w').write(r.text)

    except Exception, e:
        print e

#make_request("http://www.hp.com", tempfile.mktemp())

for host_url in fileinput.input():
    t = threading.Thread(target=make_request,
                     args=("http://"+host_url.rstrip(), tempfile.mktemp()))
    t.start()

for t in threading.enumerate():
    if t is not threading.currentThread():
        t.join()

print "end of the main thread"

