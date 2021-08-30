from os import listdir

path = 'archivos_discharge_s'
names = listdir(path)
contadorT = 0

for archivo in names:
    file = open(path+"/"+archivo)
    data = file.read()
    posT1 = data.find('tracheotomy')
    posT2 = data.find('Tracheotomy')
    posT3 = data.find('tracheostomy')
    posT4 = data.find('Tracheostomy')
    if (posT1 == -1 and posT2 == -1 and posT3 == -1 and posT4 == -1):
        print (f'El paciente del archivo {archivo} no presenta ni presentó una condición clínica asociada con traqueotomía')
    else:
        contadorT = contadorT + 1

print (f'El número de pacientes que  tienen o tuvieron una condición clínica asociada con traqueotomía es de: {contadorT}')