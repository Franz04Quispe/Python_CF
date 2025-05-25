"""
CLASES EN PYTHON

Se usa la nomenclatura PascalCase : MiClase
class <NombreClase>():
    ...

<variable> = NombreClase()

HERENCIA
Otras clases pueden heredar atributos de la clase padre
"""
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False

class Admin(User):
    # Sobre escritura de metodos en las clases hijas
    def __init__(self, username, password, email):
        super().__init__(username, password)
        self.email = email

    def send_email(self):
        print(">>> Enviando correoa a: ", self.email)

    def login(self, username, password):
        if super().login(username, password):
            self.send_email()
        else:
            print("NOO")

class Organizer(User):
    ...

admin = Admin("Admin1", "password1", "ad@pk.net")
org = Organizer("Organizer1", "password2")

print(admin.login("Admin1", "password1"))
print(admin.username, admin.password)

print(org.login("Organizer", "password2"))
