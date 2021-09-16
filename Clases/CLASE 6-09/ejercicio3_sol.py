# escriba un código que reciba un string como input y cambie por $
# todas las ocurrencias de su primera letra, excepto ella misma
# que no debe cambiar.
# primero pruebe que funcione con todas minusculas,
# ejemplo: araña quedaría ar$ñ$
# luego pruebe que funcione con la primera en mayúscula,
# ejemplo: Araña quedaría Ar$ñ$

word = input("Escriba una palabra: ")
firstChar = word[0]
firstCharAux = word[0].lower()
word = word.replace(firstCharAux, '$')
word = firstChar + word[1:]
print(word)
