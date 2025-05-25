"""
FUNCIONES EN PYTHON
Su estructura básica es la siguiente:   
def nombre_funcion(parametros):
    # Código de la función
    return resultado
"""

# 1. VALORES POR NOMBRE Y POSICIÓN
def full_name(first_name, last_name, prefix):
    full_name = f"{prefix} {first_name} {last_name}"
    return full_name

# Asignando valores a los parámetros, por nombre
print(full_name(
    first_name="Leoncio", 
    last_name="Guerra", 
    prefix="Mr."))

# Asignando argumentos, por posicion
print(full_name("Franz", "Quispe", "Sr.")) # Llama a la función


# 2. VALORES POR DEFECTO, pueden colocarse valores por default en los parametros
# Se asigna los valores de derecha a izquierda OJO
def calculate_total(price, tax=0.05, discount=0):
    total = price + (price * tax) - discount
    return total

# Con descuento
total = calculate_total(100, 0.08, 10)
print("Total", total)

# Sin descuento, pero como el parametro tiene su valor por default
total = calculate_total(100, 0.08)
print("Total", total)

# Sin tax ni descuento, pero como los parametros tienen sus valores por default
total = calculate_total(100)
print("Total", total)

# Asignando en los argumentos los valores de los parametros
total = calculate_total(
    price=200, 
    tax=0.09, 
    discount=15)
print("Total", total)