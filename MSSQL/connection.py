import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AVIJIT;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()