"""
CLASES EN PYTHON

Se usa la nomenclatura PascalCase : MiClase
class <NombreClase>():
    ...

<variable> = NombreClase()

METODOS
"""
class User:
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email
    
    def say_hello(self):
        print("HOLA SOY FRANZ", self.username)

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.say_hello
            return True
        return False

user1 = User(
    username="Joel",
    password="56s",
)

user1.say_hello()
user1.login("Joel","56s")

# ATRIBUTOS PRIVADOS, como tal no existen en Python
# Solo se añade un prefijo de guion bajo: _atributo
# EX: self._atributo

# Tambien podemos usar el Name Mangling con doble guion bajo antes de un atributo