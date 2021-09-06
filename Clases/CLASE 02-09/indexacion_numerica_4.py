import numpy as np
var = np.array([50,55,60,65,70,75,80,85,90,95,100,105])

# la indexación no solo sirve para seleccionar una porción de la variable.
# También podemos modificar el valor en sus posiciones:

# Asignemos un cero a las posiciones 4, 5 y 6
ind = [4, 5, 6]
var[ind] = 0
print(f'nuevo var: {var}')

# multipliquemos las posiciones 4, 5 y 6 por 100
var = np.array([50,55,60,65,70,75,80,85,90,95,100,105])
ind = [4, 5, 6]
var[ind] = var[ind]*100
print(f'nuevo var: {var}')

# Asignemos un cero a las posiciones pares
ind = np.arange(0, len(var), 2)
var[ind] = 0
print(f'nuevo var: {var}')

# multipliquemos las posiciones pares por 100
var = np.array([50,55,60,65,70,75,80,85,90,95,100,105])
ind = np.arange(0, len(var), 2)
var[ind] = var[ind]*100
print(f'nuevo var: {var}')

