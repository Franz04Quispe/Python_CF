"""
DICCIONARIOS EN PYTHON
Los diccionarios son estructuras de datos que almacenan pares de clave(llave)-valor. No se rigen por el orden de los indexes, sino por las claves.
Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación.
Se crean de la siguiente manera:
variable = {
    "clave1": valor1,
    "clave2": valor2,
    ...
}
Las llaves en los diccionarios son únicas, lo que significa que no se pueden repetir. Si se intenta agregar una clave que ya existe, el valor anterior se sobrescribirá.
Las llaves pueden ser: string, tplas, int, float, booleans y funciones
"""
user = {
    "name": "Franz",
    "age": 25,
    "is_student": True,
    "courses": ["Python", "Java", "C++"],
    "address": {
        "street": "123 Evergreen St",
        "city": "Springfield",
        "state": "OH",
    }
}
# Acceder a los valores de un diccionario
print(user["name"])  # Accede al valor de la clave "name"
print(user["address"]["city"])  # Accede al valor de la clave "city" dentro de "address"

user2 = {
    10 : "Franz",
    3.14: "Pi",
    True: "Boolean",
    (1, 2): "Tuple",        
}
# Funciona pero no es recomendable
print(user2[True])  # Accede al valor de la clave 10

# Obtener elementos
print("name" in user)  # Verifica si la clave "name" existe en el diccionario

# Obtener elementos usando get("variable", "Mensaje de error")
user_name = user.get("as", "NO EXISTE")  # Obtiene el valor de la clave, si no existe devuelve None
print(user_name)

# Añadir elementos a un diccionario, este se añade al final del diccionario
user["email"] = "petardo@net.css"
print("Añadiendo: ",user)

# METODOS DE DICCIONARIOS
# keys() -> Devuelve una vista de las claves del diccionario
print("- Uso de keys()")
print(user.keys())  # Devuelve una vista de las claves del diccionario
print(tuple(user.keys()))  # Convierte la vista de claves en una tupla

# values() -> Devuelve una vista de los valores del diccionario
print("- Uso de values()")
print(user.values())  # Devuelve una vista de los valores del diccionario
print(list(user.values()))  # Convierte la vista de valores en una lista

# items() -> Devuelve una vista de los pares clave-valor del diccionario
print("- Uso de items()")
print(user.items())  # Devuelve una vista de los pares clave-valor del diccionario
print(list(user.items()))  # Convierte la vista de pares clave-valor en una lista de tuplas

# ACTUALIZAR ELEMENTOS
user["name"] = "Franzito"  # Actualiza el valor de la clave "name"
print("Actualizando: ",user)

# Uso de update() -> Actualiza el diccionario con los pares clave-valor de otro diccionario
user.update({
    "name": "Frank", 
    "age": 26})  # Actualiza el diccionario con los pares clave-valor de otro diccionario
print("Actualizando con update: ",user)

# Metodo setdefault() -> Devuelve el valor de la clave si existe, si no existe, añade la clave con el valor por defecto
user.setdefault("id", 100)
print("Añadiendo con setdefault: ",user)  # Añade la clave "id" con el valor 100

# Eliminar elementos con del
del user["is_student"]  # Elimina la clave "is_student" del diccionario
print("Eliminando: ",user)

# Eliminar elementos con pop() -> Elimina la clave y devuelve el valor
user_email = user.pop("email")  # Elimina la clave "email" del diccionario y devuelve el valor
print("Eliminando con pop: ",user)  