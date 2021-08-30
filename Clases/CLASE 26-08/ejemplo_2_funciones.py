import numpy as np

# función sort, sirve para ordenar los elementos del array, por defento lo hará de manera ascendente, sin embargo, es posible modificar el orden

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

print(np.sort(arr))


# funcion concatenate sirve para concatenar o sumar 2 arrays. La salida es un único array con los elementos de los 2 arrays de entrada

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

print(np.concatenate((a, b)))

# que pasa con arrays de multiples dimensiones, se genera una matriz con n dimensiones, donde n es la suma de las dimenciones de los arrays concatenados

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

print(np.concatenate((x, y)))

# si se tiene la siguiente matriz

array_example = np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],
[[0, 1, 2, 3],[4, 5, 6, 7]],[[0 ,1 ,2, 3],[4, 5, 6, 7]]])

# ndarray.ndim le dirá el número de ejes o dimensiones de la matriz.

print(array_example.ndim)

# ndarray.size le dirá el número total de elementos de la matriz. Este es el producto de los elementos de la forma de la matriz.

print(array_example.size)

# ndarray.shape mostrará una tupla de números enteros que indican el número de elementos almacenados a lo largo de cada dimensión de la matriz. 
# Si, por ejemplo, tiene una matriz 2-D con 2 filas y 3 columnas, la forma de su matriz es (2, 3).

print(array_example.shape)

# Con la función reshape es posible cambiar la "forma" es decir las dimensiones de un array o una matriz, SE DEBE TENER EN CUENTA que la 
# combinación de ejes debe tener la misma cantidad de elementos al array original. Es decir si tento un array de 1D con 12 elementos y 
# quiero cambiarle la forma a 2D debo tener los mismos 12 elementos, debería entonces tener un reshape de 3 filas y 4 columnas

a = np.arange(12)
print(a)
b = a.reshape(3, 4)
print(b)

