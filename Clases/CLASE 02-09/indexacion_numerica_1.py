# Recordemos el manejo de índices y slicing
# con strings
var = 'Algoritmos y estructura de datos'
print('La primera letra es: ' + var[0])
print('La última letra es: ' + var[-1])
print('Las primeras 3 letras son: ' + var[0:3])
print('Las primeras 3 letras son: ' + var[:3])
print('Las últimas 3 letras son: ' + var[-3:])

# con listas
var2 = [10, 20, 40, 80, 160, 320, 640, 1280]
print('Con listas:')
print(var2[0])
print(var2[-1])
print(var2[0:3])
print(var2[:3])
print(var2[-3:])

# con una lista transformada en ndarray
var2 = [10, 20, 40, 80, 160, 320, 640, 1280]
import numpy as np
var2 = np.array(var2)
print('Con ndarray a partir de listas:')
print(var2[0])
print(var2[-1])
print(var2[0:3])
print(var2[:3])
print(var2[-3:])

# con un ndarray de Numpy a partir de arange
var3 = np.arange(-10, 11, 1)
print('Con ndarray:')
print(var3)
print(var3[0])
print(var3[-1])
print(var3[0:3])
print(var3[:3])
print(var3[-3:])