"""
FUNCIONES EN PYTHON
Las funciones son las herramientas que nos permiten realizar tareas específicas dentro de un programa.
Las funciones son bloques de código que se pueden reutilizar y que pueden recibir parámetros de entrada y devolver resultados.
Las funciones solo deben realizar una tarea específica, y no deben ser demasiado largas o complejas.
Su estructura básica es la siguiente:   
def nombre_funcion(parametros):
    # Código de la función
    return resultado
"""
# 1. FUNCIONES SIN PARÁMETROS
def say_hello():
    print("Hola, mundo!")

def say_bye():
    print("Adiós, mundo!")

# LLamadas a las funciones
say_hello() # Llama a la función
say_bye() # Llama a la función

# 2. FUNCIONES CON PARÁMETROS
def count_to(number):
    for n in range(number):
        print(n)
# Llamada a la función, con el argumento que se almacenará en el parámetro
count_to(10) # Llama a la función

def multiply(number1, number2):
    result = number1 * number2
    print(f"El resultado de multiplicar {number1} por {number2} es {result}")

multiply(5, 10) # Llama a la función


def full_name(first_name, last_name,prefix):
    full_name = f"{prefix} {first_name} {last_name}"
    print(f"El nombre completo es: {full_name}")

full_name("Franz", "Quispe", "Sr.") # Llama a la función

# 3. FUNCIONES CON RETORNO DE VALORES
def add(number1, number2):
    return number1 + number2

print(add(5, 10)) # Llama a la función y muestra el resultado

def divide(number1, number2):
    if number2 == 0:
        return "No se puede dividir entre cero"
    else:
        return number1 / number2
    
print(divide(10, 2)) # Llama a la función y muestra el resultado

# 4. RETORNAR MULTIPLES VALORES
def foo():
    return "Cody", True, 12 

# Desempaquetar el resultado de la función
username, active, age = foo() # Llama a la función y almacena el resultado en variables
print(username, age) # Llama a la función y muestra el resultado