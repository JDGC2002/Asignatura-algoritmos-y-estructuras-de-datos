from datetime import date

my_date = date(1996, 12, 11)
print("La fecha ingresada es: ", my_date)

# Error 1: poner los parámtros como string:
# my_date = date("1996", 12, 11)
# print("La fecha ingresada es: ", my_date)

# Error 2: valores fuera de rango (mes 13...)
# my_date = date(1996, 13, 11)
# print("La fecha ingresada es: ", my_date)

# accediendo a atributos: año, mes y día:
print(my_date.year)
print(my_date.month)
print(my_date.day)

# la fecha actual:
my_date = date.today()
print("La fecha de hoy es: ", my_date)

# para crear fecha desde un string con formato YYYY-MM-DD:
new_date = date.fromisoformat("2000-05-20")
print(new_date)