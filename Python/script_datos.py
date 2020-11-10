import mysql.connector
from datetime import datetime
import random

def add_user(name, age):
  query_data = (name, age, )
  query = (f"INSERT INTO usuario (nombre, edad) values (%s,%s);")
  cursor.execute(query, query_data)
  cnx.commit()

def add_register(user, types, register):
  date = datetime.now()
  query_data = (user, types, register, date, )
  query = (f"INSERT INTO registros (id_persona, tipo_registro, registro, fecha) values (%s,%s,%s,%s);")
  cursor.execute(query, query_data)
  cnx.commit()

try:
  cnx = mysql.connector.connect(user='root', password='kokoloco', host='127.0.0.1', database='iot_reto', auth_plugin='mysql_native_password')
  cursor = cnx.cursor()
  
  # while(True):
  #   print(" \n-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n")
  #   print("1. Agrega un usuario.")
  #   print("2. Agrega un Registro.")
  #   print("3. Salir.")
  #   opcion = int(input("Escoge la opción: "))
  #   if(opcion == 1):
  #     name = input("Nombre: ")
  #     age = int(input("Edad: "))
  #     add_user(name, age)

  #   elif(opcion == 2):
  #     user = input("Ingresa el numero de usuario. ")
  #     types = int(input("1. Ritmo Cardiaco.\n2. Oxigenación.\n Ingrese tipo de registro: "))
  #     if (types == 1):
  #       types = "Ritmo Cardiaco"
  #       register = random.randint(60, 100)
  #     else:
  #       types = "Oxigenación"
  #       register = random.randint(87, 96)
  #     add_register(user, types, register)
  #   else:
  #     break
  
  for i in range(5000):
    user = random.randint(1, 3)
    types = random.randint(1, 2)
    if (types == 1):
      types = "Ritmo "
      register = random.randint(60, 100)
    else:
      types = "Oxige"
      register = random.randint(87, 96)
    add_register(user, types, register)

except mysql.connector.Error as err:

  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
finally:
  cnx.close()
