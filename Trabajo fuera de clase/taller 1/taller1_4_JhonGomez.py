import csv
from os import close
import numpy as np

def BuscadorMaxArea():
    '''
    Dado un departamento, se recibirá el municipio con mayor área de este
    '''
    file = open("Municipality_Area_mod.csv", encoding="UTF-8")
    files = open("Municipality_Area_mod.csv", encoding="UTF-8")
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
        i = i+1
        if dep == depAnt:
            listmun.append(mun)
        else:
            depMun[depAnt] = listmun
            listmun = []
            listmun.append(mun)
            i = 0
    DepartamentoEleccion = input('Elige el departamento: ')
    municipios = depMun[DepartamentoEleccion]
    listaAreas = []
    i = 0
    liness = csv.DictReader(files, delimiter=',')
    for aux in liness:
        if aux['Municipio'] == municipios[i]:
            mun = aux['Municipio']
            area = aux['Area (km2)']
            munArea[mun] = int(area)
            i = i+1
            if i==len(municipios):
                i = 0
    i = 0
    for municipio in municipios:
        listaAreas.append(int(munArea[municipio]))
        i = i+1
    posArea = (listaAreas.index(max(listaAreas)))
    return print(f'El municipio con mayor área de {DepartamentoEleccion} es {municipios[posArea]}')

intento = BuscadorMaxArea()   



