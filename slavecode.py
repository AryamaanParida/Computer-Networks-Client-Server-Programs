import socket
serverAddressPort   = ("127.0.0.1", 9999)
bufferSize          = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


while (True):
    msgFromClient = input("The command :")
    bytesToSend = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
   
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Server says: {}".format(msgFromServer[0].decode())

    if('Connection rescinded' in msg):
    	break
    print("Server Output: ")
    f=open('display.txt','r')
    print(f.read()) 

UDPClientSocket.close()



