# escriba un código que transforme una lista de entrada con palabras
# en una variable tipo string con las palabras separadas por
# espacios.
# ejemplo:
# entrada: ["Hola", "a", "todos"]
# salida: "Hola a todos"

# Sol 1
wordsList = ["Hola", "a", "todos"]
words = ""
for i in wordsList:
    words = words + i + " "
print(words)
#print(words[:-1])

# Sol 2
# wordsList = ["Hola", "a", "todos"]
# words = "-"
# words = words.join(wordsList)
# print(words)