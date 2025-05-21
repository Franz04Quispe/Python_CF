"""
STRINGS EN PYTHON
Los strings son una secuencia de caracteres.
En Python, los strings son inmutables, lo que significa que no se pueden cambiar una vez creados. Sin embargo, se pueden crear nuevos strings a partir de los existentes.
Los strings son objetos inmutables
"""
print("Strings en Python")
message = "Hola, mundo!"
print(message,type(message),len(message))

print("Caracter en cadena: ","a" in message)# Devuelve True si el carácter está en la cadena
print("Caracter en la posicion: ",message.index('o')) # Devuelve la posición de la primera aparición de un carácter 

# Slicing en  strings
message2 = "hh" + message[1:]
print(message2)