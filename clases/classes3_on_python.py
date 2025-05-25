"""
CLASES EN PYTHON

Se usa la nomenclatura PascalCase : MiClase
class <NombreClase>():
    ...

<variable> = NombreClase()

PROPERTIES
"""
class User:
    def __init__(self, username, password, email=None, rol="Organizer"):
        self.username = username
        self._password = password # Privado, solo en la clase
        self.email = email

        self.rol = rol

    # El uso del decorador property
    @property
    def password(self): #lectura
        if self.rol == "Admin":
            return self._password

        return None  
    
    # Para modificar el atributo privado
    @password.setter
    def password(self, new_password):
        if self.rol == "Admin":
            self._password = new_password

user1 = User(
    username="Joel",
    password="56s",
    rol="Admin"
)

print(user1.password)
user1.password = "afa"
print(user1.password)