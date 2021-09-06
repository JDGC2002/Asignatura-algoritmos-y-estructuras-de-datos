
# Esto no funciona como uno pensaría:
var = [20, 21, 23, 20, 18, 18]
ind = var == 20
print(ind)
# observemos que ind no es un array de booleanos, es solo un valor booleano.
# cuando estas operaciones lógicas se hacen sobre una lista, no aplican elemento
# por elemento. 
# la solución en este caso es:
import numpy as np 
var = np.array([20, 21, 23, 20, 18, 18])
ind = var == 20
print(ind)


# En la indexación numerica, esto no funciona:
# var = [50,55,60,65,70,75,80,85,90,95,100,105]
# ind = np.arange(0,10,2)
# print(var[ind])
# No se puede usar una variable ind de tipo ndarray para una var que es tipo lista.
# en este caso debemos pasar var a tipo ndarray
var = np.array([50,55,60,65,70,75,80,85,90,95,100,105])
ind = np.arange(0,10,2)
print(var[ind])

# en la indexación booleana con strings, esto no funciona:
#¿Cuantas letas "a" tiene la siguiente frase?
frase = 'Hay que estudiar algortimos y estrucutura de datos con moral'
#ind = frase == 'a'
#print(f'Número de letas "a": {sum(ind)}')
# una solución, pero que ya no tiene que ver son indexación es:
print(f'Número de letas "a": {frase.count("a")}')