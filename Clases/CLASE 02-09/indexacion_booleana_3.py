import numpy as np

# la variable ind (booleana) nos sirve para realizar operaciones
# segmentando partes de la variables, veamos algunos ejemplos:

# notas de una quiz para 10 estudiantes
notas = np.array([4.6, 2.8, 3, 3.2, 3, 4.3, 4.3, 2.6, 1.5, 4.6])

# ¿cuantas personas ganaron el quiz?
ind = notas >= 3
out1 = notas[ind]
print(f'El quiz lo ganaron: {len(out1)}')

# ¿cuantas personas ganaron el quiz? (otra forma)
ind = notas >= 3
print(f'El quiz lo ganaron: {sum(ind)}')

# ¿cuál es la nota promedio de los que ganaron el quiz?
ind = notas >= 3
out2 = notas[ind]
notaPromedio = round(np.mean(out2),2)
print(f'La nota promedio de los que ganaron: {notaPromedio}')

# ¿cuantas personas sacaron nota entre 4 y 5?
ind1 = notas >= 4
ind2 = notas <= 5
ind = ind1 & ind2
out3 = notas[ind]
print(f'Sacaron entre 4 y 5: {len(out3)} personas')

# Nota promedio de los que sacaron entre 4 y 5
ind1 = notas >= 4
ind2 = notas <= 5
ind = ind1 & ind2
out3 = notas[ind]
notaPromedio = round(np.mean(out3),2)
print(f'La nota promedio de los quesacaron entre 4 y 5: {notaPromedio}')