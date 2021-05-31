import socket
import subprocess
import os
localIP     = "127.0.0.1"
localPort   = 9999
bufferSize  = 1024


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server is waiting for clients")


while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Client says:{}".format(message)
    clientIP  = "Client's IP Address:{}".format(address)

    if('Quit' in message.decode()):
    	UDPServerSocket.sendto("Connection rescinded".encode(), address)
    	break
    
    os.system(message.decode())
    os.system(message.decode()+'>>display.txt')
    UDPServerSocket.sendto("Command has been executed".encode(), address)

UDPServerSocket.close()
	





