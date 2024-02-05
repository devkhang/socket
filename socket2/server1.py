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

def recvList(conn):
    List = []
    item = conn.recv(1024).decode(format)
    while(item != 'end'):
        List.append(item)
        conn.sendall(item.encode(format))
        item = conn.recv(1024).decode(format)
    return List

try:
    conn,address = s.accept()
    print('client address : ',address,'connected')
    print('conn : ',conn.getsockname())
    mes = None
    while(mes != 'x'):
        # mes = conn.recv(1024).decode(format)
        # print('client ',address,'say',mes)
        # if mes == 'x':
        #     break  # Kết thúc vòng lặp khi người dùng nhập 'x'
        # mes = input('server response :')
        # conn.sendall(mes.encode(format))
        mes = conn.recv(1024).decode(format)
        print("client ",address, "says", mes)
        if (mes == "list"):
            #response
            conn.sendall(mes.encode(format))
            list = recvList(conn)

            print("received: ")
            print(list)
except:
    print('error')

print('END')
input()
conn.close()
