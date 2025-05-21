"""
STRINGS EN PYTHON
Busqueda en Listas - Metodos
"""
title = "Curso profesional de Python "

print("profesional" in title)

# Estandarizando el string, convirtiendo a minusculas los caracteres del string
print("curso" in title.lower(), title.lower())

# Estandarizando el string, convirtiendo a mayusculas los caracteres del string
print("curso" in title.upper(), title.upper())

# Usando el metodo count(), retorna la cantidad de veces que se repite el string
print(title.count("o"))

# Usando el metodo startswith(), retorna si inicia con el carater como argumento
print(title.startswith("C"))

# Usando el metodo endswith(), retorna si inicia con el carater como argumento
print(title.endswith("o"))

# Usando el metodo strip(), elimina los espacios en blanco al inicio y al final del string
print(title.strip())

# Usando el metodo find(), retorna la posicion del primer caracter que se repite
print(title.find("p"))

# Usando el metodo isnumeric(), retorna True si el string es numerico
print("123".isnumeric())
print("Franz".isnumeric())

# Usando el metodo capitalize(), convierte el primer caracter a mayuscula
message = "codigo facilito"
print(message.capitalize())
print(f"{message[0].upper()}{message[1:]}") # Usando el indexado
# Usando el metodo title(), convierte el primer caracter de cada palabra a mayuscula
