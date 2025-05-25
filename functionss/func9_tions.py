"""
FUNCIONES EN PYTHON
Su estructura básica es la siguiente:   
def nombre_funcion(parametros):
    # Código de la función
    return resultado

DECORADORES
A(B) ->C
A (Decorador)
B (Funcion a decorar (Base))
C (Funcion decorada Base + Nuevas lineas de codigo)
""" 
#               B
def decorator(func): #A

    def wrapper(): #C
        print(">>> Antes del llamado")
        func()
        print(">>> Antes del llamado")

    return wrapper

@decorator
def hello_world(): #B
    print("HOLA MUNDO")

hello_world()

