import socket
import json

IP = '127.0.0.1' #this ip is the ip
to talk to self
port = 12345
sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
#this socket is using udp

addr = sock.bind((IP, port))
users = {}

print(f"Listening from port {port}") #f string format. dont worry just
printing

def register(users, header, address): #method for accepting usernames. users is a list of usernames. prints users
	users[header['handle']] = address
	temp = 'users: '
	for keys, value in users.items():
		temp += keys + ' '
	print(temp)

def leave(users, header): #method for logging out. removes user from list. prints users
	users.pop(header['handle'])
	temp = 'users: '
	for keys, value in users.items():
		temp += keys + ' '
	print(temp)

def sendMsg(users, header):
	print(f'[From {header["handle"]} To {header["destination"]}]:{header["message"]}')
	dest = users[header['destination']]
	header = json.dumps(header).encode('utf-8')
	sock.sendto(header, dest)

def sendAll(users, header):
	temp = header['handle']
	header = json.dumps(header).encode('utf-8')

	for i in users:
		if (i == temp):
			pass
		else:
			dest = users[i]
			sock.sendto(header, dest)

def main():
	connected = True

	while connected:
		header, address = sock.recvfrom(1024)
		#receive header from client

		header = header.decode('utf-8')
		header = json.loads(header)
		temp = header['command'].strip().split(" ")
		temp = temp[0]

		if (temp == '/leave'):
			print(f'{header["handle"]} disconnected')
			leave(users, header)
		elif (temp == '/register'):
			register(users, header, address)
			print(f'Welcome, {header["handle"]}!')
		elif (temp == '/msg'):
			sendMsg(users, header)
		elif (temp == '/all'):
			sendAll(users, header)
		elif (temp == '/join'):
			header["message"] = 'joined'
			header = json.dumps(header).encode('utf-8')
			sock.sendto(header, address)
	sock.close()

main()