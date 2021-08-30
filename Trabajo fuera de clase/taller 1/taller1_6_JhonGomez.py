import pandas as pd 

df = pd.read_csv('Municipality_Area.csv')

depSearch = input('Indique el nombre del departamento: ')
areaSearch = int(input('Indique el valor de área en km2: '))

departamentos = df[df['Departamento']==depSearch]
areas = departamentos[departamentos['Area (km2)']> areaSearch]
municipios = areas['Municipio'].values

if len(municipios)>0:
    print (f'Los municipios del departamento {depSearch} con un área mayor a {areaSearch} km2 son: {municipios}')
else:
    print (f'En el departamento de {depSearch} no hay municipios con un área mayor a {areaSearch} km2')