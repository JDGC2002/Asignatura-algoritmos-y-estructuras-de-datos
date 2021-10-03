import csv

file = open("Municipality_Area.csv", encoding="UTF-8")

munAreas = {}

lines = csv.DictReader(file, delimiter=',')
for aux in lines:
    mun = aux['Municipio']
    area = aux['Area (km2)']
    munAreas[mun] = area

munSearch = input('Indique el nombre del municipio: ')
print(munAreas[munSearch])
