import sqlite3 as sq
from sqlite3.dbapi2 import connect

#conectarme a una base de datos

conect = sq.connect('ejemplo.db')
print('Conectado a ejemplo.db')

conect.close()
print('Desconectado a ejemplo.db')
