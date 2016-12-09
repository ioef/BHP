#!/usr/bin/env python
import getpass
import sys
import paramiko
import subprocess

def ssh_command(ip, port, user, passwd, command):

	client = paramiko.SSHClient()

	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, port, username=user, password=passwd)
     
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.exec_command(command)
		print ssh_session.recv(1024)
	return



def main():
	
	if len(sys.argv[1:]) != 3:
		print "Usage: ./bh_sshcmd.py server port username"
		sys.exit(0)

	server   = sys.argv[1]
	port     = int(sys.argv[2])
	username = sys.argv[3]
	
	password = getpass.getpass("Password:")
	ssh_command(server, port,  username, password, 'id')

if __name__=="__main__":
	main()

