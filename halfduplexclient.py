from socket import *
server_name = 'localhost'
server_port = 9999
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

while True:
  sentence = input("Client Says: ")
  client_socket.send(sentence.encode())
  message = client_socket.recv(2048)
  print ("Server says: ", message.decode())
  if(sentence == 'Exit'):
    client_socket.close()