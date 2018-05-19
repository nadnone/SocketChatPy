import socket
import sys

print('C''est parti !')

ipHote = '';
portHote = 1;

while True:
	
 	ipHote = raw_input('IP de lecture: ')
	portHote = input('Port de lecture: ')

	if portHote != 1:
		if ipHote != '':
			break 

	
# creation socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IP, TCP
sock.bind((ipHote, portHote))
sock.listen(1)
print('Attente de connexion sur : IP => ' + ipHote + ' Port => ' + str(portHote))

try:
	while True: # si quelque chose passe dans la lecture

		leFlux, adresseClient = sock.accept()
		print '\n\nConnexion accepte avec : ' + adresseClient[0] + ':' + str(adresseClient[1]) + '\n'

		while True: #si la connexion est accepte		

			leFlux.sendto('Ton message : ', adresseClient)
			reception = leFlux.recv(2048)
			print('Message recu de ' + adresseClient[0] + ':' + str(adresseClient[1]) + ' => ' + reception)

			if not reception :
				print('Deconnexion de : ' + adresseClient[0])
				break
		
			

		leFlux.close()
		print('Flux coupe')

finally:
	sock.close()
	print('fin')
