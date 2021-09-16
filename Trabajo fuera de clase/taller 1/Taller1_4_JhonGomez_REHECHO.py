import csv 
file = open("Municipality_Area_mod.csv", encoding="UTF-8")

def Maxmun():
    '''
    Escriba un departamento y recibirá el municipio de mayor área del mismo.
    '''

    depArea = {}
    depMun = {}
    listArea = []
    listMun = []
    i = 0
    lines = csv.DictReader(file, delimiter=',')

    for aux in lines:
        if (i==0):
            depAnt = aux['Departamento']
        dep = aux['Departamento']
        mun = aux['Municipio']
        area = int(aux['Area (km2)'])
        i = i+1
        if dep == depAnt:
            listMun.append(mun)
            listArea.append(area)
        else:
            depArea[depAnt] = listArea
            depMun[depAnt]= listMun
            listMun = []
            listArea = []
            listArea.append(area)
            listMun.append(mun)
            i = 0
    
    depSearch = input('Escriba el departamento y recibirá su municipio con mayor area: ')
    return print(f"El municipio de mayor area es {(depMun[depSearch])[(depArea[depSearch]).index((max(depArea[depSearch])))]}")

munSearcher = Maxmun()