import pandas as pd
import numpy as np

df = pd.read_csv('notas.csv')
cols = df.columns #observe esta variable en modo debug
notas_df = df[cols[1:]] #solo las notas (los números), listo?

# convertir a ndarray de Numpy forma 1
notas = notas_df.values
# convertir a ndarray de Numpy forma 2
notas = notas_df.to_numpy()

# Calcule la nota final para cada estudiante. El resultado debe ser un
# ndarray con la nota de cada uno.
porcentajes = np.array([0.15 , 0.15 , 0.25 , 0.15 , 0.30])
notafinal = np.zeros(len(notas))
listaNotas = np.zeros(len(notas))
contador = 0
contador2 = 0

for nota in notas:
    for calificacion in nota:
        calificacionP = calificacion*(porcentajes[contador])
        notafinal[contador] = calificacionP
        sumaNotas = np.sum(notafinal)
        contador = contador + 1
        if contador==5:
            listaNotas[contador2] = sumaNotas
            contador2 = contador2 + 1
            contador = 0
            notafinal =  np.zeros(len(notas))


print(listaNotas)

