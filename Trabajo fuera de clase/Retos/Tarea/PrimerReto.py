def estado_vacunacion (edad, comorbilidades, covidReciente):
    condicion1 = edad>=12 and edad<35
    condicion2 = comorbilidades == True
    condicion3 = edad>=35
    condicion4 = covidReciente == 0 or covidReciente > 90

    if (((condicion1 and condicion2) or condicion3) and condicion4):
        print ('Te puedes vacunar')
    elif (condicion1 == False and condicion3 == False):
        print('No te puedes vacunar porque eres menor a 12 años')
    elif (condicion1 == True and condicion2 == False):
        print('No te puedes vacunar porque eres menor a 35 años y no tienes presencia de comorbilidades')
    elif (((condicion1 and condicion2) or condicion3) and condicion4 == False):
        print ('No te puedes vacunar porque has tenido covid en los últimos 3 meses (90 días)')

estado_vacunacion (12, True, 0)
estado_vacunacion (38, True, 97)
estado_vacunacion (35, False, 97)
estado_vacunacion (11, True, 0)
estado_vacunacion (13, False, 0)
estado_vacunacion (13, True, 27)
estado_vacunacion (35, True, 29)