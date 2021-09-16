# escriba un código que reorganice las letras de una palabra
# empezando por las minusculas y continuando por las 
# mayúsculas.
# ejemplo: AlGoritMos quedaría loritosAGM
word = 'AlGoritMos'
wordmin = []
wordmay = []
for x in word:
    if x.islower() == True:
        wordmin.append(x)
    else:
        wordmay.append(x)

newWord = ''.join(wordmin + wordmay)
print(newWord)