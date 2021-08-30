# Formas de crear sets
Days=set(["Mon", "Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)
input("Press Enter to continue...")

# Acceder a sus elementos (ojo no permite usar índices)
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
for d in Days:
   print(d)
input("Press Enter to continue...")

# Adicionar un elemento
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Days.add("Sun")
print(Days)
input("Press Enter to continue...")

# Eliminar un elemento
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Days.discard("Sun")
print(Days)
input("Press Enter to continue...")

# Union de sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA | DaysB
print(AllDays)
input("Press Enter to continue...")

# Intersección de sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)
input("Press Enter to continue...")

# Diferencia de sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
print(AllDays)
input("Press Enter to continue...")

# Comparación de sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)