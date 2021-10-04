from os import name
import sqlite3 as sq
from sqlite3.dbapi2 import Cursor

#pasos para usar y manipular una base de datos:
# 1) Conectarme
# 2) Definir cursor y modificar
# 3) Guardar o asigna esa modificación
# 4) Cerrar la conexión


#conectarme a una base de datos

conexion = sq.connect('ejemplo.db')
print('Conectado a ejemplo.db')

# definir cursor
cursor = conexion.cursor()
print(cursor)

# Modificacion: crear tabla
# En MAYUSCULA lo que es fijo y se debe escribir siempre, en minúscula lo que es propio de nosotros
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGRER, nombre VARCHAR(100), correo VARCHAR(100), salario INTEGRER)')

#para borrar la tabla, se usa DROP TABLE y lo que le sigue es el nombre de la tabla
#cursor.execute('DROP TABLE usuarios')

#Insertar datos a la tabla usuarios
#cursor.execute("INSERT INTO usuarios VALUES (1000644865, 'David Alejandro Gómez', 'gomez.david@uces.edu.co', 200000)")

#Leer datos de la tabla
# para leer una entrada de la tabla, el asterisco es porque se están leyendo todos los atributos
cursor.execute('SELECT * FROM usuarios')
usuario = cursor.fetchone()
print(usuario)

#Leer atributos específicos
cursor.execute('SELECT nombre, correo FROM usuarios')
usuario = cursor.fetchone()
print(usuario)

#Para buscar usuarios en particular por diferentes campos
#cursor.execute('SELECT * FROM usuarios WHERE nombre = David Alejandro Gómez')
usuario = cursor.fetchall()
print(usuario)

#Guardar los cambios que hicimos
conexion.commit()

#cerrar conexión:
conexion.close()
print('Desconectado a ejemplo.db')
