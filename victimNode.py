from socket import *
import sys

def main():
	if len(sys.argv) != 2:
		print('error')
	else:
		ip = sys.argv[1]
		port = 12000
		sock = socket(AF_INET, SOCK_DGRAM)
		sock.bind((ip, port))

		while True:
			data_recv, c_address = sock.recvfrom(1)
		

if __name__ == '__main__':
	main()
