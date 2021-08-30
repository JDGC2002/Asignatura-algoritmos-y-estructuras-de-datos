import csv

file = open("Municipality_Area.csv", encoding="UTF-8")

depArea = {}
AreaList = []
i = 0

lines = csv.DictReader(file, delimiter=',')
for aux in lines:
    if (i==0):
        depAnt = aux['Departamento']
    dep = aux['Departamento']
    area = aux['Area (km2)']
    i = i+1
    if dep == depAnt:
        AreaList.append(area)
    else:
        depArea[depAnt] = AreaList
        AreaList = []
        i = 0

depSearch = input('Escriba el departamento y recibirá el área total de este: ')
areatot = sum(map(int, (depArea[depSearch])))
print (f'El área total del departamento: {depSearch} es de {areatot} km2')