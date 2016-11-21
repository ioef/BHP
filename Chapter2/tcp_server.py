#!/usr/bin/env python

#A simple multithreaded TCP Server

import socket
import sys 
import threading

def handle_client(client_socket):
	
	# print out what the client sends
	request = client_socket.recv(1024)
	
	print "[*] Received: %s" % request
	
	#send back a packet
	client_socket.send("ACK!")
	
	print "[*] Sent: ACK!"
	client_socket.close()


def main():

	#bind on all interfaces
	bind_ip="0.0.0.0"
	#bind on port 9999
	bind_port = 9999

	#create the socket 
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#bind the server	
	server.bind((bind_ip,bind_port))


	# listen with a maximum backlog of 5 connections
	server.listen(5)

	print "[*] Listening on %s:%d" % (bind_ip, bind_port)


	

	#$don't serv forever! Serve until 
	while True:
		
		client, addr = server.accept()
	
		print "[*] Accepted connection from: %s:%d" %(addr[0], addr[1])

		#spin up our client thread to handle incoming data
		client_handler = threading.Thread(target=handle_client, args=(client,))
	
		client_handler.start()

if __name__ == '__main__':
	main()
