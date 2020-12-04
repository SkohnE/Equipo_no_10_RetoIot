import mysql.connector
import datetime
import random

def fecha_Aleatoria():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date
  
def add_user(name, age, weight):
  query_data = (name, age, weight)
  query = (f"INSERT INTO Usuario (nombre, edad, peso) values (%s,%s,%s);")
  cursor.execute(query, query_data)
  cnx.commit()

def add_register_ritmo(user, register, date):
  query_data = (user, register, date, )
  query = (f"INSERT INTO Ritmo_Cardiaco (id_usuario, ritmo_cardiaco, fecha) values (%s,%s,%s);")
  cursor.execute(query, query_data)
  cnx.commit()

def add_register_oxigeno(user, register, date):
  query_data = (user, register, date, )
  query = (f"INSERT INTO Oxigenacion (id_usuario, oxigenacion, fecha) values (%s,%s,%s);")
  cursor.execute(query, query_data)
  cnx.commit()

try:
  cnx = mysql.connector.connect(user='root', password='kokoloco', host='127.0.0.1', database='Reto', auth_plugin='mysql_native_password')
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
    user = random.randint(1, 6)
    rit = random.randint(50, 110)
    oxi = random.randint(86, 96)
    fecha = fecha_Aleatoria()
    add_register_ritmo(user, rit, fecha)
    add_register_oxigeno(user, oxi, fecha)



except mysql.connector.Error as err:
  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
finally:
  cnx.close()
