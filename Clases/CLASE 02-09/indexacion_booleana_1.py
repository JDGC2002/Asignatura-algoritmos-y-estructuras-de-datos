import numpy as np
var = np.array([50,55,60,65,70,75,80,85,90,95,100,105])

# la indexación booleana nos permite acceder o modificar las posiciones de una variable
# a partir de otra variable (booleana) o de una operación lógica que la genere.

# ¿cómo quedarnos con solo con las posiciones 3, 4, 7, 10?
ind = [False,False,False,True,True,False,False,True,False,False,True,False]
out1 = var[ind]
print(f'posiciones seleccionadas: {out1}')

# ¿qué pasa si ind no tiene el mismo tamaño de var?
# ind = [False,False,False,True]
# out1 = var[ind]
# print(f'nuevo var: {out1}')

# multipliquemos las posiciones 3, 4, 7, 10 por 100
ind = [False,False,False,True,True,False,False,True,False,False,True,False]
var[ind] = var[ind]*100
print(f'nuevo var: {var}')



