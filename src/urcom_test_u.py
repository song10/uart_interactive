'''
Created on 2010/11/1

@author: song10
'''

#import os
#import time
import sys
import socket
import select
import argparse

def isStdin():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def isSocket(soc):
	return select.select([soc], [], [], 0) == ([soc], [], [])

def main ():
	parser = argparse.ArgumentParser(description='Translate a Virtual Emulation Platform (VEP) file into a SID configuration file.')
#	parser.add_argument('file', metavar='FILE', type=file, nargs=1, help='VEP file name')
#	parser.add_argument('-d', '--database', required=True, help='the file name of component definition database')
	parser.add_argument('-p', '--port', type=int, default=8888, help='the file name of output data (default: stdio)')
	args = parser.parse_args()

	HOST = '127.0.0.1' # Symbolic name meaning all available interfaces
	PORT = args.port   # Arbitrary non-privileged port
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.connect((HOST, PORT))
	#soc.setblocking(0) # non-blocking

	while True :
		if isStdin() :
			rd = sys.stdin.readline()
			soc.send(str.encode(rd))
	
		# RX (serial)
		if isSocket(soc) :
			ch = soc.recv(1)
			sys.stdout.write(bytes.decode(ch))
	
if __name__ == '__main__':
	main()
