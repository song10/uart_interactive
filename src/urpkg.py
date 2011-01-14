'''
Created on 2011/1/14

@author: song10
'''

import sys
import select
import argparse
import serial

def isStdin():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def isSocket(soc):
	return select.select([soc], [], [], 0) == ([soc], [], [])

def main ():
	parser = argparse.ArgumentParser(description='UART packet tester.')
	parser.add_argument('file', metavar='FILE', type=file, nargs=1, help='packet content file')
	parser.add_argument('-s', '--size', type=int, default=16, help='the size of a packet include 2-byte packet number (default: 16 byte)')
	parser.add_argument('-i', '--interval', type=int, default=10, help='interval between packets (default: 10 ms)')
	parser.add_argument('-m', '--mode', default='play', help='play or loopback mode (default: play)')
	parser.add_argument('-p', '--port', default='COM1', help='COM port (default: COM1)')
	parser.add_argument('-b', '--baudrate', default=38400, type=int, help='baudrate (default: 38400)')
	parser.add_argument('-t', '--timeout', default=0, type=int, help='timeout (default: 0 non-blocking mode)')
	args = parser.parse_args()

	print('port="%s", baudrate="%d", timeout="%d"'%(args.port, args.baudrate, args.timeout))
	ser = serial.Serial(args.port, args.baudrate, timeout=args.timeout) #0 for non-blocking

	chucksize = args.size
	if chucksize < 5:
		chucksize = 5
	if  chucksize > 2048:
		chucksize = 2048
	chucksize -= 2
	packetnum = 0
	infile = args.file
	while True:
		packet = infile.read(chucksize)
		if "" == packet:
			break
		
		packet = "%2d"%packetnum + packet
		ser.write(packet)
		print(packet)
		packetnum += 1

if __name__ == '__main__':
	main()
	