import numpy as np
var = np.array([50,55,60,65,70,75,80,85,90,95,100,105])

# la variable ind (booleana) generalmente no se genera manualmente.
# veamos algunas formas:

# ¿cómo quedarnos con solo con las posiciones donde el valor es mayor a 70?
ind = var > 70
print(f'nuestro ind: {ind}')
out1 = var[ind]
print(f'Valores mayores a 70: {out1}')

# ¿donde el valor es mayor a 70 y menor a 90?
# ind = 70 < var < 90
# print(f'nuestro ind: {ind}')
# out2 = var[ind]
# print(f'Valores mayores a 70: {out2}')

# así sí:
ind1 = var > 70
ind2 = var < 90
ind = ind1 & ind2
print(f'nuestro ind: {ind}')
out2 = var[ind]
print(f'Valores mayores a 70 y menores a 90: {out2}')

# si algún valor es 65, multiplicarlo por 100
ind = var == 65
print(f'nuestro ind: {ind}')
var[ind] = var[ind]*100
print(f'nuevo var: {var}')
