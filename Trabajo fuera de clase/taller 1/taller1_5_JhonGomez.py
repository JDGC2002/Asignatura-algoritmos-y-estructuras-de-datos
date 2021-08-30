import pandas as pd 

df = pd.read_csv('Municipality_Area.csv')

depSearch = input('Indique el nombre del departamento: ')

aux1 = df[df['Departamento']==depSearch]
aux2 = aux1['Area (km2)']
aux3 = aux1.iloc[aux2.argmax()]['Municipio']

print (f'El municipio de mayor área del departamento {depSearch} es: {aux3}')

#MUN_MAX_AREA = df.iloc[df['Departamento'] == depSearch][df['Area (km2)'].argmax()]['Municipio']
#print (f'El municipio de mayor área del departamento {depSearch} es: {MUN_MAX_AREA}')
