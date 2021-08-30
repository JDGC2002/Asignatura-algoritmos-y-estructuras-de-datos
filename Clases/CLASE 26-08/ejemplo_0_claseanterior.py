import numpy as np

# Crear un array de valores int
array1 = np.array([10,20,30,40,50])

# Acceder a ciertos elementos por su posición
print (array1[0])
print (array1[2])
input("Press Enter to continue...")

# Insertar un elemento en la posición indicada
array1 = np.insert(array1,1,60)
for x in array1:
   print(x)
input("Press Enter to continue...")

# Eliminar un elemento en la posición indicada
array1 = np.array([10,20,30,40,50])
array1 = np.delete(array1,2)
for x in array1:
   print(x)
input("Press Enter to continue...")

# Eliminar el primer elemento que corresponda al valor indicado
array1 = np.array([10,40,20,40,30,40,50])
for i in range(len(array1)):
   if array1[i] == 40:
      array1 = np.delete(array1,i)
      break
print(array1)
input("Press Enter to continue...")

# Eliminar todos los elementos que correspondan al valor indicado
array1 = np.array([10,40,20,40,30,40,50])
pos = []
for i in range(len(array1)):
   if array1[i] == 40:
      pos.append(i)
array1 = np.delete(array1,pos)
print(array1)
input("Press Enter to continue...")

# Actualizar el valor de un elemento en la posición indicada
array1 = np.array([10,20,30,40,50])
array1[2] = 80
for x in array1:
   print(x)
input("Press Enter to continue...")

# Encontrar TODAS posiciones de un elemento por su valor (todas las ocurrencias)
array1 = np.array([10,40,20,40,30,40,50])
pos = np.where(array1==40)
for x in pos:
   print(x)
input("Press Enter to continue...")

# Encontrar la posición de un elemento por su valor (primera ocurrencia)
array1 = np.array([10,40,20,40,30,40,50])
pos = np.where(array1==40)
print(pos[0][0])
input("Press Enter to continue...")

# ¿Cómo sumar dos arrays?
array1 = np.array([10,20,30,40,50])
array2 = np.array([1,2,3,4,5])
array3 = array1 + array2
print(array3)