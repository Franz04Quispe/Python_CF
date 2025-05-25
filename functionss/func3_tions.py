"""
FUNCIONES EN PYTHON
Su estructura básica es la siguiente:   
def nombre_funcion(parametros):
    # Código de la función
    return resultado
"""
# Para funciones con muchos parametros, 
# son prefijos por lo que van antes del parametro
# Para recibir una cantidad indefinida de valores de entrada

# A. * (Manejamos los valores de entrada mediante posicion)
# Ejemplo 1
def suma(*numbers):
    return sum(numbers) #Usando la funcion sum

print(suma(10,20,30), type(suma))

# Ejemplo 2
def show_info(username, email, *scores):
    print(username)
    print(email)

    average = sum(scores) / len(scores)
    print(average)

show = show_info(
    "Franz",
    "fra@as.bo",
    10,10,8,9,9,5,10 #Tupla
)
print(show, type(suma))

# B. ** (Manejamos los valores de entrada mediante nombres)
def show_i(**user):
    for key,value in user.items():
        print(key, "-", value)
# LLamada a la funcion
show_i(
    username="Franz Joel",
    email="123@pk.net",
    password="123",
    active=True,
    courses=["Python", "PHP", "Java"]
)