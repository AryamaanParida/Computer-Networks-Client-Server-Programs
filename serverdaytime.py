import socket
import time
from threading import Thread 

def thread():
	while True:
		data = conn.recv(1024)
		print('Client Communication :' + data.decode())
		if ('Exit' in data.decode()) or not data:
			print("Communication Terminated")
			conn.close()
			break
		elif('Time' in data.decode()):
			st = time.asctime( time.localtime() )
			print ("Local current time and date :", st)
			conn.sendall(st.encode()) 
			continue
		else:
			print('Server reply:',end='')  
		
		
			st=input()
			conn.sendall(st.encode())  

host = '127.0.0.1'
port = 9999
s = socket.socket()		
s.bind((host,port))
s.listen(2)

print("Waiting for client/s")
while True:
	conn,addr = s.accept()	        
	print("Client connected with address: ", addr)
	pr = Thread(target=thread)
	pr.start()

conn.close()