import numpy as np

# 1. ¿Cuantas personas tienen 18 años?
edades = np.array([18, 18, 17, 18, 20, 21, 23, 20, 18, 18, 19, 21])

# 2. ¿Cuantas personas tienen 20 o más años?

ind = edades>=20
print(f'Hay {sum(ind)} personas con 20 o más años')

# 3. ¿Cuantas personas tienen entre 17 y 19 años?

ind1 = edades>=17
ind2 = edades<=19
ind = ind1 & ind2
out2 = edades[ind]
print (f'Hay {len(out2)} personas con una edad entre 17 y 19 años')

# 4. ¿Cuál es la edad promedio de los menores de 23 años?

ind = edades<23
out3 = edades[ind]
edadPromedio = round(np.mean(out3))
print (f'La edad promedio entre aquellos menores a 23 años es: {edadPromedio}')

# 5. A los mayores de 22 años asignarles edad igual a cero.

ind = edades>22
edades[ind] = 0
print(edades)

# 6. A los que tengan 18 o 20 años asignarles una edad de 100.
edades = np.array([18, 18, 17, 18, 20, 21, 23, 20, 18, 18, 19, 21])

ind1 = edades==18
ind2 = edades==20
ind = ind1 | ind2
edades[ind] = 100
print(edades)

# 7. Genere un print que haga la función de tabla de frecuencias así:
#    cantidad 17 años: 1
#    cantidad 18 años: 5
#    cantidad 19 años: 1
#    cantidad 20 años: 2
#    cantidad 21 años: 2
#    cantidad 22 años: 0
#    cantidad 23 años: 1

edades = np.array([18, 18, 17, 18, 20, 21, 23, 20, 18, 18, 19, 21])
for i in range(17,24):
    ind = edades == i
    print(f'cantidad {i} años: {sum(ind)}')
