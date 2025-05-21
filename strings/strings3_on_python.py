"""
STRINGS EN PYTHON
Generar nuebos strings
"""
# 1. Generar un string a partir de otro string
name = "Franz"
last_name = "Quispe"

full_name = name + " " + last_name
print("1.",full_name, "/",type(full_name), len(full_name))

# 2. Generar un string a partir de una lista
full_name = "_".join([name, last_name])
print("2.",full_name, "/",type(full_name), len(full_name))

# 3. Utilizando %s 
full_name = "%s %s" % (name, last_name)
print("3.",full_name, "/",type(full_name), len(full_name))

# 4. Utilizando format(), permite usar otros tipos de datos
# Utiliza placeholders en {} pueden tener nombres de variables
full_name = "{} {} la edad es {}".format(name, last_name, 24)
print("4.",full_name, "/",type(full_name), len(full_name))

# 5. Utilizando f-strings (Python 3.6+), permite usar otros tipos de datos
# Permite usar expresiones dentro de los {}
full_name = f"{name} {last_name} la edad es {28}"
print("5.",full_name, "/",type(full_name), len(full_name))

# PRINT usadno el parametro sep, lo que hace es separar los argumentos
print("El nombre completo es:", name, last_name, sep=" - ")