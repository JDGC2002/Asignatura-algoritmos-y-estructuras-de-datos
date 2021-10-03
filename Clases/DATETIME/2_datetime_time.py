from datetime import time
  
my_time = time(13, 24, 56)
print("Tiempo ingresado: ", my_time)
  
# Puedo solo ingresar un argumento:
my_time = time(minute = 12)
print("Tiempo solo con minutos: ", my_time)
  
# Si llamo sin argumentos creo con ceros:
my_time = time()
print("variable con ceros: ", my_time)

# Algunos atributos:
my_time = time(11, 34, 56) 
print("hour =", my_time.hour)
print("minute =", my_time.minute)
print("second =", my_time.second)
print("microsecond =", my_time.microsecond)

