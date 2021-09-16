from datetime import datetime

# strptime para convertir string con fechas en datetime objects
new_datetime = datetime.strptime("2007/08/25", "%Y/%m/%d")
print(new_datetime)

# fecha con formato de Estados Unidos
new_datetime = datetime.strptime("08/25/2007", "%m/%d/%Y")
print(new_datetime)

# fecha con formato libre
date_string = "25 August, 2007"
new_datetime = datetime.strptime(date_string, "%d %B, %Y")
print(new_datetime)

# fecha con formato libre y con horas, minutos y segundos
date_string = "18:55:00, 25 August, 2007"
new_datetime = datetime.strptime(date_string, "%H:%M:%S, %d %B, %Y")
print(new_datetime)

# fecha con formato libre y con horas, minutos y segundos en formato AM/PM
date_string = "06:55:00 PM, 25 August, 2007"
new_datetime = datetime.strptime(date_string, "%I:%M:%S %p, %d %B, %Y")
print(new_datetime)

# recordar strftime()