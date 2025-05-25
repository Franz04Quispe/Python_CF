"""
DOCSTRINGS, en la primera linea del bloque de la funcion entre comillas triples, va una pequeña descripcion
"""
# Ejemplo 1
def full_name(firs_name, last_name):
    """Permite generar un nombre completo.
    
    Args:
        - first_name (String)
        - last_name (String)

    Return:
        String
    """
    return f"{firs_name} {last_name}"
# Con esta linea imprimimos el Docstring
print(full_name.__doc__)

result = full_name("Franz", "Quispe")
print(result)

# Ejemplo 2, probar codigo mediante comentarios
# En la terminal de esta forma: python -m doctest func10_tions.py
# Se puede ver  que con las 3 >>> simulamos la terminal de python en el codigo. No retornara nada si la funcion esta bien.
def palindromo(sentence):
    """Permite conocer si un strng es o no, un palindromo
    
    Args: 
        - sentemce (String)

    Return:
        - Bool

    Examples:
    >>> palindromo("oso")
    True

    >>> palindromo("Anita lava la tina")
    True

    >>> palindromo("CodigoFacilito")
    False
    """
    sentence = sentence.lower().replace(" ","")
    return sentence == sentence[::-1]