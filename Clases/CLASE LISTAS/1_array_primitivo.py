from array import *

# Crear un array de valores int
array1 = array('i', [10,20,30,40,50])

# Acceder a ciertos elementos por su posición
print (array1[0])
print (array1[2])
input("Press Enter to continue...")

# Insertar un elemento en la posición indicada
array1.insert(1,60)
for x in array1:
   print(x)
input("Press Enter to continue...")

# Eliminar un el primer elemento que corresponda al valor indicado
array1.remove(40)
for x in array1:
   print(x)
input("Press Enter to continue...")

# Eliminar un elemento en la posición indicada
array1.pop(2)
for x in array1:
   print(x)
input("Press Enter to continue...")

# Actualizar el valor de un elemento en la posición indicada
array1 = array('i', [10,20,30,40,50])
array1[2] = 80
for x in array1:
   print(x)
input("Press Enter to continue...")

# Encontrar la posición de un elemento por su valor (primera ocurrencia)
array1 = array('i', [10,20,30,40,50])
print (array1.index(40))
input("Press Enter to continue...")

# Encontrar TODAS posiciones de un elemento por su valor (todas las ocurrencias)

array1 = array('i', [40,10,20,40,30,40,50])
for i in range(len(array1)):
   if (40 == array1[i]):
      print (i)

# ¿Cómo sumar dos arrays?
array1 = array('i', [10,20,30,40,50])
array2 = array('i', [1,2,3,4,5])
array3 = array1 + array2
print(array3)
input("Press Enter to continue...")

# mmmm eso no era lo esperado... ¿entonces?

array3 = []
for i in range(len(array1)):
   array3.append(array1[i]+array2[i])
print(array3)