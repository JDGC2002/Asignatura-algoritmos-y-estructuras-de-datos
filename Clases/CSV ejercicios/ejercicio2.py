#crear un diccionario con los nombres de los departamentos como keys
#y una lista con los municipios como value. para probar pida con un input un nombre
#de un departamento e imprima sus municipios

import csv

file = open("Municipality_Area.csv", encoding="UTF-8")

depMun = {}
listmun = []
i = 0

lines = csv.DictReader(file, delimiter=',')
for aux in lines:
    if (i==0):
        depAnt = aux['Departamento']
    dep = aux['Departamento']
    mun = aux['Municipio']
    i = i+1
    if dep == depAnt:
        listmun.append(mun)
    else:
        depMun[depAnt] = listmun
        listmun = []
        listmun.append(mun)
        i = 0

depSearch = input('Escriba el departamento y recibirá los municipios de este: ')
print (depMun[depSearch])
