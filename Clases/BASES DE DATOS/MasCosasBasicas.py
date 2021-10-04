import sqlite3 as sq

conexion = sq.connect('ejemplo.db')
cursor = conexion.cursor()

#Ingresar varios datos de una sola vez
usuarios = [(40524976, 'Pablo Montoya', 'batistuta12@gmail.com', 30000, 22), (45231896, 'Mariana Arroyo', 'Marr@outlook.es', 50000, 35), (1001564821, 'Elizabeth Cardenas', 'eli12@hotmail.com', 200000, 44)]

#sentencia para ingresarlos
# los interrogantes son la cantidad de atributos
#cursor.executemany('INSERT INTO usuarios VALUES (?,?,?,?,?)', usuarios)
# print('usuarios añadidos')

# Leer muchos datos
# cursor.execute('SELECT * FROM usuarios')

# usuariosBD = cursor.fetchall()
# for i in usuariosBD:
#     print(i)

#Actualizar datos de todos los usuarios existentes
#cursor.execute('UPDATE usuarios set salario = 100000')

#Actualizar datos de todos los usuarios existentes
#cursor.execute('UPDATE usuarios set salario = 150000 WHERE id = 1000644865')

#Eliminar datos particulares
#cursor.execute('DELETE FROM usuarios')

# Agregar columnas (Campos)
#cursor.execute('ALTER TABLE usuarios ADD edad INTEGRER')
#cursor.execute('INSERT INTO usuarios VALUES (4562314856, "Pablo Motos", "PABLOM@hotmail.es", 500000, 60)')

#Eliminar columnas
#cursor.execute("ALTER TABLE usuarios DROP COLUMN edad")

conexion.commit()
conexion.close()