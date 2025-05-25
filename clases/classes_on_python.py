"""
CLASES EN PYTHON

Se usa la nomenclatura PascalCase : MiClase
class <NombreClase>():
    ...

<variable> = NombreClase()
"""
# Forma no convencional o no recomendada
class User:
    username = ""
    password = ""
    email = ""

# Instanciar objetos
user1 = User()
user2 = User()
user3 = User()

# Modificar los atributos del objeto
user1.username = "Franz"
user1.email = "fr@pk.net"
user1.password = "secretfr"

user2.username = "Luis"
user2.email = "lu@pk.net"
user2.password = "secretlu"

user3.username = "Andres"
user3.email = "an@pk.net"
user3.password = "secretan"

print(user1.username, user1.email, user1.password)
print(user2.username, user2.email, user2.password)
print(user2.username, user2.email, user2.password)


# Forma convencional o recomendada
# con el metood init
class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

usuario1 = Usuario(
    username="Franchesco",
    password="151",
    email="fr@pk.net"
)

# Atributos Dinamicos
usuario1.is_admin = True
usuario1.courses = [
    "Python", "PHP", "Java"
]

print(usuario1.username, usuario1.password, usuario1.email)

print(usuario1.is_admin)
print(usuario1.courses)
# Imprime el diccionario de los atributos de la clase
print(usuario1.__dict__)