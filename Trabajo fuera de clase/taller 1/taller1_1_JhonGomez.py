from os import listdir

path = 'archivos_discharge_s'
names = listdir(path)
contadorM = 0
contadorF = 0

for archivo in names:
    file = open(path+"/"+archivo)
    data = file.read()
    posSex = data.find('Sex')
    if (posSex == -1):
        print (f'Hay un error en el archivo: {archivo}')
    else:
        textoSexo = data[posSex:data.find('Service')]
        if (textoSexo.count('M') == True):
            contadorM = contadorM + 1
        elif (textoSexo.count('F') == True):
            contadorF = contadorF + 1

print (f'El número de hombres es: {contadorM} ; el número de mujeres es: {contadorF}')
