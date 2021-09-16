# escriba un código que reciba una frase como input conformada por varias
# palabras. Realice un print que diga cuál es la más larga y cuál es
# su número de caracteres.
# ejemplo: "Mi materia favorita es algoritmos y estructura de datos"
# el resultado sera: 
# La palabras más larga es: algoritmos
# su tamaño es: 10.0

sentence = str(input('Escriba la frase que quieras: '))
sentence = sentence.split(' ')
print(f'La palabra más larga es: {max(sentence, key=len)}')
print(f'su tamaño es: {len(max(sentence, key=len))}')