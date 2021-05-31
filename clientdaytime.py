import socket
def client():
	
	s=socket.socket()
	
	host='127.0.0.1'
	port=9999
	s.connect((host,port))
	while(True):
		num=(input())
		if(num == 'Exit'):
			s.close()
			break
		
		s.send(num.encode())
		data=s.recv(1024).decode()
		print('This is the received from Server: '+ data)
		
client()