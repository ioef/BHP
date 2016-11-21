#!/usr/bin/env python

import socket 
from optparse import OptionParser

#Script that can retrieve info from webservers equivalent to the netcat utility with the GET Request
#$ nc hostname 80 
#  GET / HTTP/1.0 

def connect(host,port, verb=False):
	 # create a socket object for IPv4 and TCP STREAM

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
 	#connect the client
	client.connect((host,port))

	#send some data
	client.send("GET / HTTP/1.1\r\nHost: %s\r\n\r\n"% host)

	#receive some data
	response = client.recv(4096)

	if verb == True:
		print 
		print response
	else:
		print 
		response = response.split('\n')
		for line in range(0,6):
			print response[line]



def main(): 

	target_host = "www.google.com"
	target_port = 80
	verbose = False
	
	parser = OptionParser(usage='%prog host port',description="A simple tcp client")	
 	parser.add_option("-v", action="store_true", dest="verbose",  default=False, help="enable verbose output")

	(options, arguments) = parser.parse_args()
	
	if len(arguments) < 1 or len(arguments) > 2:
		parser.print_help()
		exit(1)

	target_host = arguments[0]
	
	if len(arguments) == 2:
		target_port = int(arguments[1])

	if options.verbose: verbose = True

	connect(target_host, target_port, verbose)


if __name__ == '__main__':
	main()   
