import socket
s=socket.socket()
ip="127.0.0.1"
port=9999
s.bind((ip,port))
s.listen(4)
conn,addr=s.accept()
filename=input(str("Name of the file (to be transferred): "))
file=open(filename,'rb')
data=file.read(1024)
conn.send(data)
print("File transmission is successful")