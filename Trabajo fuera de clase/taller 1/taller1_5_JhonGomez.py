import pandas as pd 

df = pd.read_csv('Municipality_Area_mod.csv')

depSearch = input('Indique el nombre del departamento: ')

departamentos = df[df['Departamento']==depSearch]
areas = departamentos['Area (km2)']
municipio = departamentos.iloc[areas.argmax()]['Municipio']

print (f'El municipio de mayor área del departamento {depSearch} es: {municipio}')


