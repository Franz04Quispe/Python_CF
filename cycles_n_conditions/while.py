from random import randint
"""
WHILE EN PYTHON
En Python, el bucle while se utiliza para ejecutar un bloque de código mientras una condición sea verdadera. La sintaxis básica es la siguiente:
while <condicion>:
    <bloque_de_codigo>

El bucle while evalúa la condición antes de ejecutar el bloque de código. Si la condición es verdadera, se ejecuta el bloque de código y luego se vuelve a evaluar la condición. Este proceso se repite hasta que la condición sea falsa.
No se conocen la cantidad de iteraciones que se van a realizar, por lo que el bucle while es útil cuando no se sabe cuántas veces se va a ejecutar el bloque de código.
"""
# 1. Ejemplo de uso de while
counter = 0
print("1. Ejemplo de uso de while")
while counter < 10:
    print("El valor del contador es: ", counter)
    counter += 1

# 2. Cuantos digitos tiene un número
number2 = int(input("Introduce un número: "))
counter2 = 0

print("2. Cuantos digitos tiene un número")
while number2 > 0:
    number2 = number2 // 10 # El operador // realiza una división entera 
    counter2 += 1   
else:
    print("El número tiene ", counter2, " dígitos")



# 3. Numero magico
num = None
random_number = randint(0, 10)
hits = 0

print("3. Numero magico")
while num != random_number and hits < 3:
    print(f"Intento número {hits}")
    num = int(input("Adivina el número mágico entre 0 y 10: "))
    if random_number > num :
        print("El número aleatorio es mayor")
    else:
        print("El número aleatorio es menor")

    hits += 1
else:
    if num == random_number:
        print(f"¡Felicidades! Adivinaste el número mágico: {random_number}")
    else:
        print(f"¡Lo siento! El número mágico era: {random_number}")