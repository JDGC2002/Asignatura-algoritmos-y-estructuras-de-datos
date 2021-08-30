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
    listmun2 = []
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
            listmun2.append(mun)
            munArea[mun] = int(area)
        else:
            depMun[depAnt] = listmun
            listmun = []
            i = 0
    DepartamentoEleccion = input('Elige el departamento: ')
    areas = np.zeros(len(depMun[DepartamentoEleccion]))
    lines = list(csv.reader(file, delimiter=','))
    for auxx in lines:
        try:
            areas[i] = int(auxx[2])
        except:
            areas[i] = 0
        i = i+1
        del lines[0]
        print(f'El municipio con mayor área de {DepartamentoEleccion} es {listmun2[(np.argmax(areas))]}')
    return None 

intento = BuscadorMaxArea()   