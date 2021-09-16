from datetime import datetime, timedelta 

ini_time = datetime.now() 
print ("initial_date", str(ini_time)) 

# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) 

# Fechas futuras sumando días... 
date_after_2yrs = ini_time + timedelta(days = 730) 
print('Fecha dos años después:  ', str(date_after_2yrs))     
date_after_30days = ini_time + timedelta(days = 30) 
print('Fecha treinta días después:  ', str(date_after_30days))     

# Fechas futuras sumando horas... 
date_after_2hrs = ini_time + timedelta(hours = 2) 
print('Fecha dos horas después:  ', str(date_after_2hrs))     

# Tiempo que ha pasado entre dos fechas: simplemente restar los dos objetos datetime
print('Diferencia de tiempo: ', str(date_after_30days - ini_time)) 

