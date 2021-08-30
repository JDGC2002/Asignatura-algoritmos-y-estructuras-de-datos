import numpy as np

# una manera de crear un array desde una lista

a = np.array([1, 2, 3, 4, 5, 6])

# Acceder a posiciones
print(a[3])

# o también es posible crear matrices

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(b[2,1])

# crear un array de ceros

print(np.zeros(2))

# crear un array de unos

print(np.ones(2))

# crear un array vacio, la función empty crea un array con valores aleatorios, los cuales dependen del estado en memoria

print(np.empty(7))

# tambien puedo crear arrays desde listas de python

print(np.arange(4))

# también puedo indicar el número inicial, final y el paso del array

print(np.arange(2, 9, 2))

