from os import listdir

path = 'archivos_discharge_s'
names = listdir(path)
contadorT = 0

for archivo in names:
    file = open(path+"/"+archivo)
    data = file.read().lower()
    if (data.count('tracheotomy') != 0 or data.count('tracheostomy') != 0):
        contadorT = contadorT+ 1
    else:
        print (f'El paciente del archivo {archivo} no presenta ni presentó una condición clínica asociada con traqueotomía')

print (f'El número de pacientes que  tienen o tuvieron una condición clínica asociada con traqueotomía es de: {contadorT}')