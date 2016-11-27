#!/usr/bin/env python
#Usage of the urllib2 library with the Request Class
#This gives as a finely grained level of control 
#on defining custome User-Agent HTTP Headers

import urllib2

url = "http://www.nostarch.com"

#create a headers Dictionary
headers = {}

headers['User-Agent'] = "Googlebot"

#create a Request Object where we pass the url and the headers dictionary
request = urllib2.Request(url, headers=headers)

#open the request and print it
response = urllib2.urlopen(request)
print response.read()

response.close()

