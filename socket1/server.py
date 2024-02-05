# import socket
# import sys

# # Create a Socket (the connection between two computers)
# def create_socket():
#     try:
#         global host
#         global port
#         global s
#         host = 'localhost'
#         port = 80
#         s = socket.socket()
#     except socket.error as msg:
#         print("Socket creation error: " + str(msg))

# # Bind the socket to a specific host and port
# def bind_socket():
#     try:
#         global host
#         global port
#         global s

#         print('Binding the port ' + str(port))
#         s.bind((host, port))
#         s.listen(5)  # Start listening for incoming connections
#     except socket.error as msg:
#         print('Socket Binding error ' + str(msg) + '\n' + 'Retrying...')
#         bind_socket()

# # Accept connections from clients
# def socket_accept():
#     conn, address = s.accept()
#     print('Connection has been established! IP: ' + address[0] + ' Port: ' + str(address[1]))
#     send_commands(conn)
#     conn.close()

# Uncomment the line below to call create_socket() function
# create_socket()

# Uncomment the line below to call bind_socket() function
# bind_socket()

# Uncomment the line below to call socket_accept() function
# socket_accept()
import socket


host = '127.0.0.1'
port = 56875
format = 'utf8'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
s.listen()

print('server side')
print('server:',host,port)
print('waiting for client!!!')

conn,address = s.accept()

print('client address: ',address)
print('conn : ',conn.getsockname())

username = conn.recv(1024).decode(format)
print('username: ',username)

respone = 'data have been taking'
conn.sendall(respone.encode(format))

pwd = conn.recv(1024).decode(format)
print('password: ',pwd)
input()