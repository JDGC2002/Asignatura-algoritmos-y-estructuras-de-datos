import sqlite3 as sq

conexion = sq.connect('restaurante.db')

# ORDERNAR

cursor = conexion.cursor()

# RESERVAS POR FECHA
# cursor.execute('SELECT * FROM reservaciones ORDER BY fecha')
# tabla = cursor.fetchall()

# for i in tabla:
#     print(i)

# AGRUPAR count id cuenta los elementos que tengan la misma fecha de reservaciones, SE AGRUPARON por fecha y ORDERNARON por cantidad de reservaciones descendente
#cursor.execute('SELECT COUNT(id), fecha FROM reservaciones GROUP BY fecha ORDER BY COUNT(id) DESC')
#tabla = cursor.fetchall()

# COMANDO INNER JOIN: se usa para relacionar tablas
#cursor.execute('SELECT * FROM platos INNER JOIN categoria ON categoria.id = platos.categoriaId')

#CONOCER la cantidad cada alimento pot categoria (cuantos desayunos, ensaladas, bebidad etc)
# cursor.execute('SELECT COUNT(id),  categoriaId FROM platos GROUP BY categoriaId')

#AHORA lo anterior pero en vez de aparecer el id de la categoria, aparece el nombre
#cursor.execute('''SELECT COUNT(platos.id),  categoria.nombre FROM platos INNER JOIN categoria ON
#platos.categoriaId = categoria.id GROUP BY categoria.nombre ORDER BY count(platos.id) ASC''')

#ORGANIZAR por precio, para ignorar duplicados se usa el comando DISTINCT
#cursor.execute('SELECT DISTINCT precio FROM platos ORDER BY precio ASC')


# ORGANIZAR por precio pero en rangos
#cursor.execute('SELECT * FROM platos WHERE precio BETWEEN 100 AND 200 ORDER BY precio DESC')

# FILTRAR POR NOMBRE
#cursor.execute('SELECT * FROM platos WHERE nombre LIKE "Vino%" ')

# comando IN traer las reservas con 2 y 3 mesas, el comando IN funciona como el between
# cursor.execute('SELECT * FROM reservaciones WHERE cantidadmesa IN (2,3)')

# TRAER todas las reservas del 2 de julio con cantidad de mesa entre 2 y 3
#cursor.execute('SELECT nombre, cantidadmesa, hora FROM reservaciones WHERE fecha = "2019-07-02" AND cantidadmesa IN (2,3)')

#tabla = cursor.fetchall()

#for i in tabla:
#    print(i)

conexion.commit()
conexion.close()