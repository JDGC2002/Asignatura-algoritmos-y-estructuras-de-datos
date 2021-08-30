list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
input("Press Enter to continue...")

# Actualizando valores en la lista
list1[2] = 2001
print(list1)
input("Press Enter to continue...")

# Insertar un elemento al final de la lista
list3 = [1, 'yo', 3]
list3.append(555) #add as a single element
print(list3)
input("Press Enter to continue...")

# Insertar un elemento en la posición indicada
list3.insert(1, 'hola') #add element i
print(list3)
input("Press Enter to continue...")

# Eliminar un elemento de la lista por su posición
list4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
del list4[5] #delete element at index 5
print(list4)
input("Press Enter to continue...")

# Eliminar un elemento de la lista por su valor
list4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
list4.remove('example') #remove element with value
print(list4)
input("Press Enter to continue...")

# Eliminar un elemento de la lista por su valor (¿qué pasa si está repetido?)
list4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
list4.remove(3) #remove element with value
print(list4)
input("Press Enter to continue...")

# Eliminar el último elemento de la lista
list4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
a = list4.pop(1) #pop element from list
print('Popped Element: ', a, ' List remaining: ', list4)
input("Press Enter to continue...")

# Eliminar todos los elementos de la lista
list4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
list4.clear() #empty the list
print(list4)
input("Press Enter to continue...")

# Concatenacion de listas (operador +)
list4 = [1, 2, 3, 'example', 3.132, 10, 3, 30]
list5 = [1, 2, 3, 10, 30, 10]
print((list4 + list5))
input("Press Enter to continue...")

# Repetición de elementos en listas
print(['hola']*4)
input("Press Enter to continue...")

# Otras funciones de listas
list5 = [1, 2, 3, 10, 30, 10]
print(len(list5)) #find length of list
input("Press Enter to continue...")

print(list5.index(10)) #find index of element that occurs first
input("Press Enter to continue...")

print(list5.count(10)) #number of ocurrences el the element in the list
input("Press Enter to continue...")

print(sorted(list5)) #print sorted list but not change original
input("Press Enter to continue...")

list5.sort(reverse=True) #sort original list
print(list5)