tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
input("Press Enter to continue...")

# NO SE PUEDE Actualizar valores en la tupla
# tup1[2] = 2001
# print(tup1)
# input("Press Enter to continue...")

# Insertar un elemento al final de la tupa
tup3 = [1, 'yo', 3]
tup3.append(555) #add as a single element
print(tup3)
input("Press Enter to continue...")

# Insertar un elemento en la posición indicada
tup3.insert(1, 'hola') #add element i
print(tup3)
input("Press Enter to continue...")

# Eliminar un elemento de la tupa por su posición
tup4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
del tup4[5] #delete element at index 5
print(tup4)
input("Press Enter to continue...")

# Eliminar un elemento de la tupa por su valor
tup4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
tup4.remove('example') #remove element with value
print(tup4)
input("Press Enter to continue...")

# Eliminar un elemento de la tupa por su valor (¿qué pasa si está repetido?)
tup4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
tup4.remove(3) #remove element with value
print(tup4)
input("Press Enter to continue...")

# Eliminar el último elemento de la tupa
tup4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
a = tup4.pop(1) #pop element from tup
print('Popped Element: ', a, ' tup remaining: ', tup4)
input("Press Enter to continue...")

# Eliminar todos los elementos de la tupa
tup4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
tup4.clear() #empty the tup
print(tup4)
input("Press Enter to continue...")

# Concatenacion de tupas (operador +)
tup4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
tup5 = [1, 2, 3, 10, 30, 10]
print((tup4 + tup5))
input("Press Enter to continue...")

# Repetición de elementos en tupas
print(('hola')*4)
input("Press Enter to continue...")

# Otras funciones de tupas
tup5 = [1, 2, 3, 10, 30, 10]
print(len(tup5)) #find length of tup
input("Press Enter to continue...")

print(tup5.index(10)) #find index of element that occurs first
input("Press Enter to continue...")

print(tup5.count(10)) #number of ocurrences el the element in the tup
input("Press Enter to continue...")

print(sorted(tup5)) #print sorted tup but not change original
input("Press Enter to continue...")

tup5.sort(reverse=True) #sort original tup
print(tup5)