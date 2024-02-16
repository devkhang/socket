import tkinter as tk
import socket
host = '127.0.0.1'
port = 56875
Login = "login"
Format = "utf8"
login = 'login'
fail = "Invalid password"
success = 'login successfully'        
class StartPage(tk.Frame):
    def __init__(self, parent, appController):
        tk.Frame.__init__(self, parent)

        label_title = tk.Label(self, text="LOG IN")
        label_user = tk.Label(self, text="username ")
        label_pswd = tk.Label(self, text="password ")

        self.label_notice = tk.Label(self,text="",bg="bisque2")
        self.entry_user = tk.Entry(self,width=20,bg='light yellow')
        self.entry_pswd = tk.Entry(self,width=20,bg='light yellow')

        button_log = tk.Button(self,text="LOG IN", command=lambda: appController.Login(self,client) ) 
        button_log.configure(width=10)
        
        label_title.pack()
        label_user.pack()
        self.entry_user.pack()
        label_pswd.pack()
        self.entry_pswd.pack()
        self.label_notice.pack()

        button_log.pack()

class HomePage(tk.Frame):
    def __init__(self, parent, appController):
        tk.Frame.__init__(self, parent)

        label_title = tk.Label(self, text="HOME PAGE")
        btn_logout = tk.Button(self, text="log out", command=lambda: appController.showPage(StartPage))

        label_title.pack()
        btn_logout.pack()        
    
class App(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)

        self.title("My App")
        self.geometry("500x200")
        self.resizable(width=False, height=False)

        #self.protocol("WM_DELETE_WINDOW", self.on_closing)

        container = tk.Frame()
        container.configure(bg="red")
        container.pack(side="top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (StartPage, HomePage):
            frame = F(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[F] = frame 


        self.frames[StartPage].tkraise()
        
    def showPage(self, FrameClass):
        self.frames[FrameClass].tkraise()
    def Login(self,currframe,sck):
        try:
            user = currframe.entry_user.get()
            pwd = currframe.entry_pswd.get()
            if(user == "" or pwd == ""):
                currframe.label_notice["text"]="field can't not be empty"
                return
            print(user,pwd)
            option = Login
            sck.sendall(option.encode(Format))
            sck.sendall(user.encode(Format))
            sck.recv(1024)
            sck.sendall(pwd.encode(Format))
            sck.recv(1024)
            msg = sck.recv(1024).decode(Format)    
            if(msg == fail):
                currframe.label_notice["text"]="invalid account"
            else:
                self.showPage(HomePage)
                
        except:
            print("Error!! server can't responding")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
print("client side")

app = App()
app.showPage(StartPage)
app.mainloop()

# import tkinter as tk
# import socket

# host = '127.0.0.1'
# port = 56875

# class StartPage(tk.Frame):
#     def __init__(self, parent, appController):
#         tk.Frame.__init__(self, parent)

#         label_title = tk.Label(self, text="LOG IN")
#         label_user = tk.Label(self, text="username ")
#         label_pswd = tk.Label(self, text="password ")

#         self.label_notice = tk.Label(self, text="", bg="bisque2")  # Điều chỉnh tên thuộc tính ở đây
#         self.entry_user = tk.Entry(self, width=20, bg='light yellow')
#         self.entry_pswd = tk.Entry(self, width=20, bg='light yellow')

#         button_log = tk.Button(self, text="LOG IN", command=lambda: appController.Login(self))  # Không cần truyền tham số client ở đây
#         button_log.configure(width=10)

#         label_title.pack()
#         label_user.pack()
#         self.entry_user.pack()
#         label_pswd.pack()
#         self.entry_pswd.pack()
#         self.label_notice.pack()

#         button_log.pack()

# class HomePage(tk.Frame):
#     def __init__(self, parent, appController):
#         tk.Frame.__init__(self, parent)

#         label_title = tk.Label(self, text="HOME PAGE")
#         btn_logout = tk.Button(self, text="log out", command=lambda: appController.showPage(StartPage))

#         label_title.pack()
#         btn_logout.pack()

# class App(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)

#         self.title("My App")
#         self.geometry("500x200")
#         self.resizable(width=False, height=False)

#         container = tk.Frame()
#         container.configure(bg="red")
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         self.frames = {}
#         for F in (StartPage, HomePage):
#             frame = F(container, self)
#             frame.grid(row=0, column=0, sticky="nsew")
#             self.frames[F] = frame

#         self.frames[StartPage].tkraise()

#     def showPage(self, FrameClass):
#         self.frames[FrameClass].tkraise()

#     def Login(self, currframe):
#         try:
#             user = currframe.entry_user.get()
#             pwd = currframe.entry_pswd.get()
#             if user == "" or pwd == "":
#                 currframe.label_notice["text"] = "Field can't not be empty"
#                 return
#             else:
#                 # Thực hiện kết nối với máy chủ
#                 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                 client.connect((host, port))  # Kết nối với máy chủ sử dụng host và port đã định nghĩa
#                 print("Connected to server successfully!")
#                 # Thực hiện các thao tác gửi dữ liệu tới máy chủ và nhận kết quả

#         except Exception as e:
#             print("Error:", e)
#             currframe.label_notice["text"] = "Error: " + str(e)

# app = App()
# app.showPage(StartPage)
# app.mainloop()
