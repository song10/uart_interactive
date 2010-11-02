'''
Created on 2010/11/1

@author: song10
'''

import socket
import sys
#import os
#import time
import select

HOST = '127.0.0.1' # Symbolic name meaning all available interfaces
PORT = 8888        # Arbitrary non-privileged port
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))
#soc.setblocking(0) # non-blocking

def isStdin():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def isSocket():
	return select.select([soc], [], [], 0) == ([soc], [], [])

while True :
#	print('x')
	if isStdin() :
#		print("y")
		rd = sys.stdin.readline()
#		print(repr(rd))
		soc.send(str.encode(rd))

	# RX (serial)
	if isSocket() :
		ch = soc.recv(1)
#		print(repr(ch))
		sys.stdout.write(bytes.decode(ch))

#	time.sleep(1)
