import socket

host = '127.0.0.1'
port = 56875
format = 'utf8'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
login = 'login'
print("client side")

def sendList(client,List):
    for item in List:
        client.sendall(item.encode(format))
        client.recv(1024).decode(format)
    item = 'end'
    client.send(item.encode(format))

def send_Account(client):
    Account = []
    username = input('username :')
    password = input('password :')
    Account.append(username)
    Account.append(password)
    sendList(client,Account)
    validCheck = client.recv(1024).decode(format)
    print(validCheck)


try:
    client.connect((host,port))
    print('client address : ',client.getsockname())

    mes = None
    while(mes != 'x'): 
        mes = input('talk :')
        client.sendall(mes.encode(format))
        # if mes == 'x':
        #     break  # Kết thúc vòng lặp khi người dùng nhập 'x'
        # mes = client.recv(1024).decode(format)
        # print('server response',mes)
        if (mes == login):
            # wait response
            client.recv(1024)
            send_Account(client)
except:
    print('error')
client.close()