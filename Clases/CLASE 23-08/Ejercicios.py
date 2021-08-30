import pandas as pd 

# #primer ejercicio hecho en clase 19/08
# df = pd.read_csv('Municipality_Area.csv')

# munSearch = input('Indique el nombre del municipio: ')

# print(df[df.Municipio==munSearch])

# #para el área de un municipio

# #Forma larga 
# aux = df[df['Municipio']==munSearch]
# print (aux.values)
# print(aux['Area (km2)'])

# #Forma corta
# print(df['Area (km2)'][df.Municipio==munSearch])

#segundo ejercicio hecho en clase 19/08

df = pd.read_csv('Municipality_Area.csv')

depSearch = input('Indique el nombre del departamento: ')

print(df[df['Departamento']==depSearch]['Municipio'].values)

#tercer ejercicio hecho en clase 19/08

#a
print(df['Area (km2)'].sum())

#b
print(df.iloc[df['Area (km2)'].argmax()])
#print(df.iloc[df['Area (km2)'].idxmax()])

#C
print(len(df['Departamento'].unique()))