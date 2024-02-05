import socket
import threading
import pyodbc

host = '127.0.0.1'
port = 56875
format = 'utf8'

con_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=MSI\SQLEXPRESS;"
            "Database=socket_Account;"
            "UID=khangmoi;"
            "PWD=123456789;")
conn = pyodbc.connect(con_str)
login = 'login'
curson = conn.cursor()
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
def handleClient(conn:socket,address):
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
        if (mes == login):
            #response
            conn.sendall(mes.encode(format))
            check_login(conn)
    print("client : ",address,'finish')
    print(conn.getsockname(),'closed')
    conn.close()
def check_login(conn):
    Account = recvList(conn)
    curson.execute("SELECT * FROM Account WHERE username = ? AND pwd = ?", Account[0], Account[1])
    data = curson.fetchall()
    mes = 'oke'
    if data:
        mes = 'login successfully'
        print("Login successfully")
    else:
        mes = "Invalid password"
        print("Login failed")

    conn.sendall(mes.encode(format))  # Đảm bảo kết thúc gửi dữ liệu


client = 0
while(client < 3):
    try:
        conn,address = s.accept()
        thr = threading.Thread(target=handleClient,args=(conn,address))
        thr.daemon = False
        thr.start()
    except:
        print('error')
    client += 1
print('END')
input()
s.close()
conn.close()