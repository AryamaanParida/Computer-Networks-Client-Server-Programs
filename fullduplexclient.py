import socket
import threading

sADDR = ('127.0.0.2')
sPort = 9999
buff = 1024

cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSock.connect((sADDR, sPort))

def receive():
    while True:
        rMessage = cliSock.recv(buff).decode()
        if (rMessage == 'exit' or not rMessage):
            print ("Connection Terminated")
            break
        print (rMessage)

def send():
    while True:
        sMessage = input(">> ")
        cliSock.send(sMessage.encode())

t1 = threading.Thread(target=send, name=1)
t2 = threading.Thread(target=receive, name=2)

t1.start()
t2.start()
