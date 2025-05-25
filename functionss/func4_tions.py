"""
FUNCIONES EN PYTHON
Su estructura básica es la siguiente:   
def nombre_funcion(parametros):
    # Código de la función
    return resultado
ARGS AND KWARGS

Por convencion todos los parametros que posean el prefijo:
    * seran llamados args
Y todos los parametros que posean el prefijo:
    ** seran llamados kwargs
"""
# Ejemplo 1
def show_info(*args, **kwargs):
    print(">>> Info")
    for value in args:
        print(value)
    print("\n")
    print(">>> Details")
    for key, value in kwargs.items():
        print(key, ":",value)

# Llamando a la funcion
print("Ejemplo 1")
show_info(
    "Franz", "Quispe", 12, "fr@pk.net",
    courses=["Pyhton", "PHP", "Java"],
    score=10,
    is_active=True,
    is_super_admin=True
)

# Ejemplo 2
def show_i(username, last_name, *args, active=True, is_super_admin=False, **kwargs):
    print("Username", username)
    print("Last name", last_name)

    print(">>>> Extra Info:")
    for value in args:
        print(value)

    print("Active", active)
    print("Super admin",is_super_admin)

    print(kwargs)

print("Ejemplo 2")
show_i(
    "Franz", "Quispe",
    "fra@gmail.com", "pass515", #args
    courses=["Pyhton", "PHP"], is_deleted=False #kwargs
)