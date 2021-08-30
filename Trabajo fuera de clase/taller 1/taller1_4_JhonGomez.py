import csv
import numpy as np

def BuscadorMaxArea():
    '''
    Dado un departamento, se recibirá el municipio con mayor área de este
    '''
    file = open("Municipality_Area.csv", encoding="UTF-8")
    lines = csv.DictReader(file, delimiter=',')
    depMun = {}
    munArea = {}
    listmun = []
    i = 0
    for aux in lines:
        if (i==0):
            depAnt = aux['Departamento']
        dep = aux['Departamento']
        mun = aux['Municipio']
        area = aux['Area (km2)']
        i = i+1
        if dep == depAnt:
            listmun.append(mun)
            munArea[mun] = int(area)
        else:
            depMun[depAnt] = listmun
            listmun = []
            listmun.append(mun)
            munArea[mun] = int(area)
            i = 0
    DepartamentoEleccion = input('Elige el departamento: ')
    municipios = depMun[DepartamentoEleccion]
    listaAreas = np.zeros(len(municipios))
    i = 0
    for municipio in municipios:
        listaAreas[i] = int(munArea[municipio])
        i = i+1
    return print(f'El municipio con mayor área de {DepartamentoEleccion} es {municipios[(np.argmax(listaAreas))]}')

intento = BuscadorMaxArea()   



