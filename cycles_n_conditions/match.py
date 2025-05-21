"""
MATCH
El uso de match es similar al switch de otros lenguajes de programación. Permite evaluar una variable y ejecutar diferentes bloques de código según su valor. La sintaxis básica es la siguiente:
match <variable>:
    case <valor1>:
        <bloque de código>
    case <valor2>:
        <bloque de código>
    ...
    case _:
        <bloque de código por defecto>
"""
score = 1
# OR en Python es el simbolo |
match score:
    case 10:
        print("Perfecto")
    case 9 | 8:
        print("Muy bien")
    case 7 | 6:
        print("Regular")
    case _:
        print("Reprobado")