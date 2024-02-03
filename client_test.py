import socket

server_addr = '/tmp/socket'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_addr)
s.send('a command here')
data = s.recv(1024)
s.close()
print ('Received'), repr(data)