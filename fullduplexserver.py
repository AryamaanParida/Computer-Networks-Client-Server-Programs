import socket
import threading

sPort = (9999)
sADDR = "127.0.0.2"
buff = 1024

servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servSock.bind((sADDR, sPort))
servSock.listen(5)

print ("Waiting for a client/s")
cliSock, cADDR = servSock.accept()
print ("Connection established with {0}".format(cADDR))

def receive():
    while True:
        rMessage = cliSock.recv(buff).decode()
        if (rMessage == 'exit' or not rMessage):
            print ("Connection Terminated")
            break
        print ((rMessage))

def send():
    while True:
        sMessage = input(">> ")
        if not sMessage:
            break
        cliSock.send(sMessage.encode())

t1 = threading.Thread(target=send, name=3)
t2 = threading.Thread(target=receive, name=4)

t1.start()
t2.start()
