import urllib
import urllib2


values = {'q' : 'python training in hyderabad'
          }

data1 = urllib.urlencode(values)
#url = 'https://www.google.com/search?' + data
url = 'http://localhost/get.php'
#print url
req = urllib2.Request(url, data="n=100")
response = urllib2.urlopen(req)
the_page = response.read()

print the_page

