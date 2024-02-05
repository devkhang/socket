import socket

host = '127.0.0.1'
port = 56875
format = 'utf8'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("client side")
client.connect((host,port))
print('client address ',client.getsockname())

username = input('username : ')

client.sendall(username.encode(format))
response = client.recv(1024).decode(format)
# print(response)

pwd = input('pwd : ')
client.sendall(pwd.encode(format))