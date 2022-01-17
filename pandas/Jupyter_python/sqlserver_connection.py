import pyodbc
import pandas as pd

server_name = 'DESKTOP-AB4GA4Q' 
database_name = 'skillqode' 
# username = 'sa' 
# password = 'sq1234'  
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;)
# cursor = cnxn.cursor()
cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server={server_name};"
                      "Database={database_name};"
                      "Trusted_Connection=yes;")
# select 26 rows from SQL table to insert in dataframe.
query = "select * from client_master ;"
df = pd.read_sql(query, cnxn)
print(df.head())