"""
CONTINUE AND BREAK
Permiten interrumpir el ciclo o continuar con la siguiente iteración
Continue: Salta a la siguiente iteración del ciclo
Break: Interrumpe el ciclo y sale de él
"""
# 1. Ejemplo de uso de continue, saltando los pares
for number in range(1, 21): # Itera del 1 al 20
    if number % 2 == 0: # Si el número es par
        continue # Salta a la siguiente iteración
    print("El número impar es: ", number)

# 2. Ejemplo de uso de continue, para pares
for n in range(1, 21): # Itera del 1 al 20
    if n % 2 != 0: # Si el número es impar
        continue # Salta a la siguiente iteración
    print("El número par es: ", n)

# 3. Ejemplo de uso de break, para salir del ciclo
for n in range(1, 21): # Itera del 1 al 20
    if n == 11: # Si el número es 11
        break # Sale del ciclo
    print("El número es: ", n)

"""
PASS
Es una instrucción nula, no hace nada
Se utiliza para evitar errores de sintaxis
"""
var = None

if var == None: # Si la variable es None
    pass # No hace nada
    ...