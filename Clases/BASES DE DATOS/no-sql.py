DATA = [{
    "nombre" : "Iker",
    "apellido" : "Casillas",
    "edad": 33,
    "posicion": ["Portero"],
    "internacional": True
},
{
    "nombre" : "Carles",
    "apellido" : "Puyol",
    "edad": 36,
    "posicion": ["Central", "Lateral"],
    "internacional": True
},
{
    "nombre" : "Ivan",
    "apellido" : "Cordoba",
    "edad": 46,
    "posicion": ["Lateral"],
    "internacional": False
}
]

import pymongo 

# PASO 1 CONECTARNOS A LA BASE DE DATOS

conexion = pymongo.MongoClient("localhost",27017)

# PASO 2 crear una BD FUTBOL

db = conexion.Futbol

# PASO 3 crear coleccion FUTBOLISTAS
coleccion = db.futbolistas

# PASO 4.1 CREAR un diccionario en la colección futbolistas
#coleccion.insert_one(DATA[0])

# PASO 4.2 CREAR muchos objetos "diccionarios" en la coleccion de futbolistas
# coleccion.insert_many(DATA)

#PASO 5 Leer dato a dato
# base_datos = coleccion.find() #con find se leen todos los datos de "coleccion"
# for i in base_datos:
#     print(i)

#PASO 5.1 Leer un solo ojeto con atributo específico
# traer solo quien juegue como "Central"

#usuario = coleccion.find({'posicion' : {'$in':['Portero']}})
# for i in usuario:
#     print(i)

#ACTUALIZAR CAMPOS de un objeto dentro de una colección
#ponemos a ivan edad de 56 años
#coleccion.update({'nombre': {'$in':['Ivan']}}, {'$set':{'edad':56}})

#ACTUALIZAR VARIOS CAMPOS POR UN ATRIBUTO SE DEBE USAR UPDATE MANY
#coleccion.update_many({'nombre': {'$in':['Iker']}}, {'$set':{'edad':77}})

#Si todos tienen ese mismo nombre, pero solo queremos modificar uno, usamos el id asignado por mongo que es único

#PASO 6 ELIMINAR
#Borrar al único con internacional : False
#coleccion.remove({'internacional': False})

#borrar a los porteros
#coleccion.delete_many({'posicion' : ['Portero']})
base_datos = coleccion.find() 
for i in base_datos:
    print(i)

