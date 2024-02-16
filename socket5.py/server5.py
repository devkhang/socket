import socket
import threading
import pyodbc

host = '127.0.0.1'
port = 56875
Format = 'utf8'

con_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=MSI\SQLEXPRESS;"
            "Database=socket_Account;"
            "UID=khangmoi;"
            "PWD=123456789;")
conn = pyodbc.connect(con_str)
login = 'login'
fail = "Invalid password"
success = 'login successfully'
curson = conn.cursor()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
s.listen()

print('server side')
print('server:',host,port)
print('waiting for client!!!')

def recvList(conn):
    List = []
    item = conn.recv(1024).decode(Format)
    while(item != 'end'):
        List.append(item)
        conn.sendall(item.encode(Format))
        item = conn.recv(1024).decode(Format)
    return List
def serverLogin(conn:socket):
    print("login start")
    username = conn.recv(1024).decode(Format)
    conn.sendall(username.encode(Format))
    pwd = conn.recv(1024).decode(Format)
    conn.sendall(username.encode(Format))
    curson.execute("SELECT * FROM Account WHERE username = ? AND pwd = ?", username, pwd)
    data = curson.fetchall()
    mes = 'oke'
    if data:
        mes = success
        print("Login successfully")
    else:
        mes = fail
        print("Login failed")

    conn.sendall(mes.encode(Format))  # Đảm bảo kết thúc gửi dữ liệu

def handleClient(conn:socket,address):
    print('conn : ',conn.getsockname())
    option = conn.recv(1024).decode(Format)
    count = 0
    while(option != 'x'and count<50):
        if (option == login):
            serverLogin(conn)
            # conn.sendall(option.encode(format))
            # check_login(conn)
            option = "x"
        count+=1
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

    conn.sendall(mes.encode(Format))  # Đảm bảo kết thúc gửi dữ liệu


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