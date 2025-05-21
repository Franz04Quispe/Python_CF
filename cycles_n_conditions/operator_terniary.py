"""
OPERADOR TERNARIO
El operador ternario es una forma concisa de escribir una expresión condicional en una sola línea. Se utiliza para asignar un valor a una variable basado en una condición. La sintaxis básica es la siguiente:
<variable> = <valor_si_verdadero> if <condicion> else <valor_si_falso>
"""

score = 10
# One liner. Operador ternario
message = "Aprobaste la materia" if score > 5 else "No aprobaste la materia"
print(message)
