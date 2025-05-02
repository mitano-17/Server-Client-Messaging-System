import socket
import json
import threading
import time
import logging

#opcommands:
#1 = login
#2 = sending message

"""
TODO
/join
/leave
/register
/all
/msg
/?
"""

sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

#this socket is using udp
header = {'handle': '', 'ip': '', 'message': '', 'destination': '', 'command': ''}

#dictionary that will be sent to server
commands = {'register': '/register <handle>', 'leave': '/leave', 'join': '/join <server_ip_add> <port>', 'all': '/all <message>', 'msg': '/msg <handle> <message>', 'help': '/?'}

def join(header):
	temp, IP, PORT = header['command'].strip().split(" ")
	PORT = int(PORT)
	ADDR = (IP, PORT)
	header = json.dumps(header).encode('utf-8')
	sock.sendto(header, ADDR)

	return ADDR

def leave(header, ADDR):
	send = json.dumps(header).encode('utf-8') #turns header to bytes before sending
	sock.sendto(send, ADDR)

	return (' ', 0)

def register(header, ADDR):
	temp, header['handle'] = header['command'].strip().split(" ")
	print('Registered!')
	send = json.dumps(header).encode('utf-8') #turns header to bytes before sending
	sock.sendto(send, ADDR)

def sendMsg(header, ADDR):
	header['message'] = header['command'].strip().split(" ", 2)[2]
	header['destination'] = header['command'].strip().split(" ", 2)[1]
	send = json.dumps(header).encode('utf-8') #dictionary is turned into bytes and sent to the server
	sock.sendto(send, ADDR)
	sock.close #close socket

def sendAll(header, ADDR):
	header['message'] = header['command'].strip().split(" ", 1)[1]
	send = json.dumps(header).encode('utf-8') #dictionary is turned into bytes and sent to the server
	sock.sendto(send, ADDR)
	sock.close

def recvMsg():
	while True:
		header = sock.recv(1024)
		header = header.decode('utf-8')
		header = json.loads(header)
		temp = header['command'].strip().split(" ")
		temp = temp[0]

		if (temp == '/all'):
			print(f'{header["handle"]}: {header["message"]}')
		if (temp == '/msg'):
			print(f'[From {header["handle"]}]: {header["message"]}')

def main():
	IP = ' '
	PORT = 0
	ADDR = (IP, PORT)
	connected = True

	while connected:
		# TODO: fix threading so client can both listen for messages and
		send messages
		# thread = threading.Thread(target = recvMsg, args = (header))
		# thread.start()
		header['command'] = input()
		temp = header['command'].strip().split(" ")
		temp = temp[0]

		try:
			joined = False
			if (temp == '/?'):
				print(commands)
			elif (temp == '/join' and ADDR == (' ', 0)):
				ADDR = join(header)
				IP, PORT = ADDR
				msg = sock.recv(1024)
				if (msg):
					print('Connection to the Message Board Server is successful!')
					joined = True
				elif (temp == '/leave'):
					print('Error: Disconnection failed. Please connect to the server first.')
				else:
					print('Error: Invalid Command/Server Not Yet Joined.')

				while joined:
					try:
						thread = threading.Thread(target=recvMsg)
						thread.start()
						header['command'] = input()
						temp = header['command'].strip().split(" ")
						temp = temp[0]

						if (temp == '/?'):
							print(commands)
						elif (temp == '/join'):
							print("You are already joined to a server.")

						if (temp == '/leave'):
							print('leave')
							ADDR = leave(header, ADDR)
							IP, PORT = ADDR
							print('Connection closed. Thank you!')
							joined = False
						elif (temp == '/register'):
							register(header, ADDR)
							print(f'Welcome, {header["handle"]}!')
						elif (temp == '/msg'):
							sendMsg(header, ADDR)
							print(f'[To {header["destination"]}]: {header["message"]}')
						elif (temp == '/all'):
							sendAll(header, ADDR)
					except ValueError:
						print("Not Enough Arguments in the Command.Use /? for more Information.")
					except ConnectionResetError:
						print("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number.")
						ADDR = (' ', 0)
					except OverflowError:
						print("Error: Invalid Port Number")
					except socket.gaierror:
						print("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number.")
					except:
						print("An error has occured.")
		
		except ValueError:
			print("Error: Not Enough Arguments in the Command / Incorrect Parameters. Use /? for more Information.")
		except ConnectionResetError:
			print("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number.")
			ADDR = (' ', 0)
		except OverflowError:
			print("Error: Invalid Port Number")
		except socket.gaierror:
			print("Error: Connection to the Message Board Server has failed! Please check IP Address and Port Number.")
		except:
			print("An error has occured.")
main()