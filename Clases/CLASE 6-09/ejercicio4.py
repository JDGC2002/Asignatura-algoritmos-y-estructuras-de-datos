# convierta la siguiente frase en un diccionario:

words = "Biomédica:35-Medicina:14-Nutrición:22-Derecho:2"
words = words.replace(':', '-')
words1 = words.split('-')
print(words1)
it = iter(words1)
res_dct = dict(zip(it, it))
print(res_dct)