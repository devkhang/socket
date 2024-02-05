import pyodbc


# print(pyodbc.drivers())

con_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=MSI\SQLEXPRESS;"
            "Database=socket_Account;"
            "UID=khangmoi;"
            "PWD=123456789;")
conn = pyodbc.connect(con_str)

curson = conn.cursor()

# for row in curson.execute("select * from Account where username = 'a'"):
#     print(row[0])
#     print(row.username)
#     print(row)
# curson.execute("select * from Account")
# data = curson.fetchall()

# print(data[0][0])
# username = 'khanghayho'
# pwd = '0936554618'
# curson.execute("insert into Account values (?,?)",username,pwd)

# conn.commit()
conn.close()
