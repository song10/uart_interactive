'''
Created on 2010/11/1

@author: song10
'''

import socket, sys, os, time
import msvcrt
import serial

def isStdin():
	return msvcrt.kbhit()

ser = serial.Serial('COM1', 38400, timeout=0) #0 for non-blocking
while True :
#	print('x')
	if isStdin() :
#		print("y")
		rd = msvcrt.getch()
		ser.write(rd)
		msvcrt.putch(rd)
#		print(repr(rd))
#		continue
#		s.send(str.encode(rd))

	ch = ser.read()
	if b'' != ch :
#		print(repr(ch))
		msvcrt.putch(ch)

#	time.sleep(1)

ser.close()
