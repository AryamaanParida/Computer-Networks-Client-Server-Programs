import socket
localIP     = "127.0.0.1"
localPort   = 12345
bufferSize  = 4096 #??
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("Server is waiting for Client")
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Client says: {}".format(message)
    clientIP  = "Client's IP Address: {}".format(address)
    print(clientMsg)
    print(clientIP)
    msgFromServer       = input("Server replies: ")
    bytesToSend         = str.encode(msgFromServer)
    UDPServerSocket.sendto(bytesToSend, address)