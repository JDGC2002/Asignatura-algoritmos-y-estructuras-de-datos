import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

# Creating a single dictionary
res = collections.ChainMap(dict1, dict2)
print(res.maps,'\n')
input("Press Enter to continue...")

# Mostrar sus keys y values
print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()
input("Press Enter to continue...")

# Print all the elements from the result
print('elements:')
for key, val in res.items():
   print('{} = {}'.format(key, val))
print()
