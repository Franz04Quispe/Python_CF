"""
FUNCIONES EN PYTHON
Su estructura básica es la siguiente:   
def nombre_funcion(parametros):
    # Código de la función
    return resultado

SCOPE - ALCANCE de las variables
Tipos de variables:
- Globales: Son aquellas que fueron creadas fuera del bloque de una funcion, puede ser usada en cualquier parte del programa
- Locales: Son aquellas que fueron creadas dentro del bloque de una funcion, y puede ser usada solo en su contexto, en su funcion
""" 
# Ejemplo de Variable global y local
username = "Franz"

def show_info():
    username = "Visca Barza" #local
    print(id(username), username)

show_info()
print(id(username), username)