import csv
import numpy as np

file = open("Municipality_Area.csv", encoding="UTF-8")
lines = list(csv.reader(file, delimiter=','))

areas = np.zeros(len(lines))
dep = []
mun = []

i = 0
for aux in lines:
    dep.append(aux[0])
    mun.append(aux[1])
    try:
        areas[i] = int(aux[2])
    except:
        areas[i] = 0
    i = i+1
    del lines[0]

search = str(input('Escoja A para el área total de Colombia , B para cual es el municipio de mayor área en colombia , C para número de departamentos: '))
print (search)
if (search == "A"):
    print (f'El área total de Colombia es: {np.sum(areas)} km2')
elif (search == "B"):
    print (f'El municipio de mayor área es: {mun[np.argmax(areas)]}') 
else:
    depLen = set(dep)
    print (f'El número de departamentos es: {len(depLen)}')


