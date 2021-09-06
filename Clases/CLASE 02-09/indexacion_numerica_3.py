import numpy as np
var = np.array([50,55,60,65,70,75,80,85,90,95,100,105])

# ¿cómo quedarnos con solo con las posiciones 3, 4, 7, 10?
#out1 = var[3,4,7,10]
#print(f'posiciones seleccionadas: {out1}')

# Así sí (listas): 
out1 = var[[3,4,7,10]]
print(f'posiciones seleccionadas: {out1}')

# visto de otra forma:
ind = [3,4,7,10]
out2 = var[ind]
print(f'posiciones seleccionadas: {out2}')

# funciona además con ndarray:
ind = np.array([3,4,7,10])
out3 = var[ind]
print(f'posiciones seleccionadas: {out3}')

# ¿cómo quedarnos con solo con las posiciones 3, 4, 7, 10 y la última?
ind = np.array([3,4,7,10,-1]) 
out4 = var[ind]
print(f'posiciones seleccionadas: {out4}')

# ¿cómo quedarnos solo con las posiciones pares? 0,2,4... pero con esta notación
ind = np.arange(0, len(var), 2)
print(f'nuestro ind: {ind}')
out5 = var[ind]
print(f'posiciones pares: {out5}')