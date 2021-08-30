# Creación de diccionario
my_dict = {} #empty dictionary
print(my_dict)
my_dict = {1: 'Python', 2: 'Java'} #dictionary with elements
print(my_dict)
input("Press Enter to continue...")

# Acceder a elementos
my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict['First']) #access elements using keys
print(my_dict.get('Second'))
input("Press Enter to continue...")

# Cambiar un valor
my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict)
my_dict['Second'] = 'C++' #changing element
print(my_dict)
input("Press Enter to continue...")

# Adicionar un par key-value
my_dict['Third'] = 'Ruby' #adding key-value pair
print(my_dict)
input("Press Enter to continue...")

# Eliminar valores
my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
a = my_dict.pop('Third') #pop element
print('Value:', a)
print('Dictionary:', my_dict)
input("Press Enter to continue...")

# Eliminar el último key-value par
b = my_dict.popitem() #pop the key-value pair
print('Key, value pair:', b)
print('Dictionary', my_dict)
input("Press Enter to continue...")

# Eliminar todos los datos del diccionario
my_dict.clear() #empty dictionary
print('n', my_dict)
input("Press Enter to continue...")

# Otras funciones
my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
print(my_dict.keys()) #get keys
print(my_dict.values()) #get values
print(my_dict.items()) #get key-value pairs
print(my_dict.get('First'))