import socket
import sys

print 'C''est parti !' 

ipServer = '127.0.0.1';
portServer = 5555;

while True:

#	ipServer = raw_input('IP d''ecriture: ')
#	portServer = input('Port d''ecriture: ')

	if ipServer != '':
		if portServer != 1:
			break


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ipServer, portServer))

try:
	while True:
		print('\n\nConnecte a : ' + ipServer + ':' + str(portServer) + '\n\n')
	
		
		reception = sock.recv(2048)
		print(reception)

		clavier = raw_input()
		clavier = clavier.decode('ascii')

		if clavier != '':
			sock.send(clavier)
	
		if not reception:
			print('le serveur ne repond pas')
			break
	


	print('Flux coupe')


finally:
	sock.close()
	print('fin')






