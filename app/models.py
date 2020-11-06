import cx_Oracle

connection = cx_Oracle.Connection("hos/hos@192.168.15.50:1521/payy")
cursor = connection.cursor()

try:
    cursor.execute("select * from wx_register")
# except cx_Oracle.DatabaseError as exc:
except Exception as err:
    print("Whoops!")
    print(err)
# print(cursor.description)
cursor.execute("select id,idcard  from wx_register")
columns = [col[0] for col in cursor.description]
cursor.rowfactory = lambda *args:dict(zip(columns, args))
data = cursor.fetchall()
print(data)
    
#print("Oracle-Error-Code:", Error.code)
#print("Oracle-Error-Message:", Error.message)