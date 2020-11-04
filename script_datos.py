import mysql.connector as mysql

try:
    cnx = mysql.connect(user='root', password='kokoloco', host='127.0.0.1', database='iot_reto')
    cursor = cnx.cursor()

    query_data = (0,)
    query = (f"SELECT * FROM cuarto WHERE id_cuarto > %s;")
    
    cursor.execute(query, query_data)

    for result in cursor:
        print(result)

except mysql.Error as err:

  if err.errno == mysql.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    
finally:
  cnx.close()
