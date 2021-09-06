import numpy as np
var = np.array([50,55,60,65,70,75,80,85,90,95,100,105])

# ¿cómo quedarnos solo con las posiciones pares? 0,2,4...
out1 = var[::2]
print(f'posiciones pares: {out1}')

# lo que es equivalente a:
out1 = var[0:len(var):2]
print(f'posiciones pares: {out1}')

# ¿cómo quedarnos solo con las posiciones impares? 1,3,5...
out2 = var[1::2]
print(f'posiciones impares: {out2}')

# ¿cómo quedarnos solo con las posiciones impares desde la 5 posición? 5,7,9...
out3 = var[5::2]
print(f'posiciones impares desde la quinta: {out3}')

# ¿cómo mostrar de 3 en 3?
out4 = var[::3]
print(f'valores de 3 en 3 posiciones: {out4}')

# ¿cómo mostrar de 3 en 3 pero desde la última hasta la primera?
out5 = var[-1::-3]
print(f'valores de 3 en 3 al revés: {out5}')