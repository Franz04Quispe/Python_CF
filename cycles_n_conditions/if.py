"""
IF
El uso de if en Python es una estructura de control que permite ejecutar un bloque de código si se cumple una condición específica.
El bloque de código dentro del if se ejecutará solo si la condición es verdadera. Si la condición es falsa, el bloque de código se omite y se continúa con la ejecución del programa.
La identacion es importante, se conforma de 4 espacios o un tabulador.
Se estructira de la siguiente manera:
if <bool>:  //si se cumple
    <bloque de código>
else:       //si no se cumple
    <bloque de código alternativo>
"""
# Recordar que se considera True un string que contenga un espacio en blanco
value = " "
print("- IF simple:")
if value:
    print("La variable tiene un valor")

# Ejemplo de uso de if y else
numer1 = 10
numer2 = 20
print("- IF y ELSE:")
# numer1 == 10 and numer2 == 20 or numer1 > numer2:
if numer1 == 10 and numer2 == 20 and numer1 > numer2:
    print("Ambas condiciones son verdaderas")
else:
    print("Una o ambas condiciones son falsas")
    print("Nos encontramos en el bloque else.")
    print("FIN DEL PROGRAMA")


# Condicionales anidadas, son condicionales dentro de otras condicionales
n1 = 10
n2 = 20
print("- Condicionales anidadas:")
if n1 >= 10:
    print("n1 es mayor o igual a 10")
    if n1 > n2:
        print("n1 es mayor n2")
    else:
        print("n1 NO ES MAYOR a n2")

# Uso de elif, que significa "else if", se utiliza para comprobar múltiples condiciones
print("- Uso de elif:")

# EVITAR CONDICIONES ANIDADAS
# color = "verde"
# if color == "verde":
#     print("Puedes pasar")
# else:
#     if color == "amarillo":
#         print("Ten cuidado")
#     elif color == "rojo":
#         print("No puedes pasar")
#     else:
#         print("Color no reconocido")

color = "amarillo"
if color == "verde":
    print("Puedes pasar")
elif color == "amarillo":
    print("Ten cuidado")
elif color == "rojo":
    print("No puedes pasar")
else:
    print("Color no reconocido")