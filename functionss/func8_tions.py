"""
FUNCIONES EN PYTHON
Su estructura básica es la siguiente:   
def nombre_funcion(parametros):
    # Código de la función
    return resultado

FUNCIONES LAMBDA - Funciones Anonimas
Carece de un nombre, no tiene uno
Su estructura tiene la palabra reservada lambda:
lambda <parametros> : <body> #Siempre retorna un valor de forma automatica
""" 
# Ejemplo 1, asignando a una variable la funcion lambda
add = lambda number1, number2=0: number1+number2

print(add(10))
print(add(10,20))
print(add(number1=50,number2=20))

# Ejemplo 2, asignando a una variable la funcion lambda


