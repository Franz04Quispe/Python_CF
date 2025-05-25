"""
FUNCIONES EN PYTHON
Su estructura básica es la siguiente:   
def nombre_funcion(parametros):
    # Código de la función
    return resultado

VARIABLES COMO FUNCIONES - Ciudadanos de primera clase
""" 
# Almacenar las funciones en variables
def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if amount > balance:
        return None
    
    return balance - amount

def default(*args, **kwargs):
    return "OPCION NO VALIDA"

options = {
    "a": deposit,
    "b": withdraw
}

option = input("Ingresa una opcion (a/b): ")
balance = int(input("Ingresa tu balance: "))
amount = int(input("Ingresa tu cantidad: "))


function = options.get(option, default)
total = function(balance, amount)
print(total)


# # Solo almacenar el nombre de la funcion, no los parentesis
# func1 = deposit
# func2 = withdraw

# # Para llamar a las funciones se escriben los nombres de las variables
# print(func1(100,20), type(func1))
# print(func2(200-50), type(func2))

