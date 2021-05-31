import socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddressPort   = ("127.0.0.1", 12345)
bufferSize          = 4096
while (True):
    msgFromClient       = input("Client says: ")
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Server replies: {}".format(msgFromServer[0])
    print(msg)
    #bytes string literal;. bytes object will be created not unicode string