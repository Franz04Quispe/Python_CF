"""
FUNCIONES EN PYTHON
Su estructura básica es la siguiente:   
def nombre_funcion(parametros):
    # Código de la función
    return resultado

FUNCIONES ANIDADAS
""" 
def outer_function():
    message = "No encontramos en una funcion anidada"

    def inner_function():
        # variable no local, esta en un bloque superior
        # se usa la palabra reservada de nonlocal
        nonlocal message 
        message = "Info value"
        
    inner_function()
    print(message)

outer_function()