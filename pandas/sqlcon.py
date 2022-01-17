import pyodbc
driver = 'SQL Server'
server = 'DESKTOP-AB4GA4Q'
db1 = 'skillqode'
tcon = 'yes'
uname = 'jnichol3'
pword = '**my-password**'

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=server;DATABASE=db1;Trusted_Connection=yes')
cursor = cnxn.cursor()
cursor.execute("select * from client_master")
rows = cursor.fetchall()
for row in rows:
    print(row)