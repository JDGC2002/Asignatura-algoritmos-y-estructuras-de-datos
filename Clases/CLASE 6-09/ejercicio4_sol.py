# convierta la siguiente frase en un diccionario:
# words = "Biomédica:35-Medicina:14-Nutrición:22-Derecho:2"

words = "Biomédica:35-Medicina:14-Nutrición:22-Derecho:2"
split1 = words.split("-")
out = {}
for i in split1:
    aux = i.split(":")
    out[aux[0]] = aux[1]
print(out)
