"""
FOR EACH
En Python existen dos tipos de ciclos o bucles: 
el ciclo for-each y el ciclo while. 
Los bucles for iteran sobre estructuras de datos basadas en colecciones como listas, tuplas y/o diccionarios.
Itera sobre cada elemento de una colección, permitiendo ejecutar un bloque de código para cada elemento.
Su estructura es la siguiente:

for <variable_que_podemos crear> in <coleccion>:
    <bloque_de_codigo>
"""
numbers = [1, 2, 3, 4, 5]
message = "Hola mundo"
user = {
    "name": "Franz",
    "age": 24,
    "password": "123"
}

# Iterar sobre una lista
for number in numbers:
    print("El valor es: ",number)

# Iterando sobre una cadena de texto
for caracter in message:
    print("El caracter es: ",caracter)

# Iternando sobre un diccionario
for key,value in user.items():
    print("La clave es:",key, "y el valor es:",value)

# USO DE RANGE
# El rango es una función que genera una secuencia de números enteros.
# Se puede usar para iterar sobre una secuencia de números.
# range(inicio, fin, paso)
# El inicio es el primer número de la secuencia.
# El fin es el último número de la secuencia.
# El paso es el incremento entre cada número de la secuencia.
# Si no se especifica el inicio, se inicia en 0.
# Si no se especifica el paso, se inicia en 1.
# Si no se especifica el fin, se inicia en 0.
# El rango se puede usar para iterar sobre una lista, tupla o diccionario.
#             range(inicio, fin, paso)
for number in range(5, 10 +1, 2):
    print("El número es: ",number)