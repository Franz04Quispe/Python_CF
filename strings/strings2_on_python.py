"""
STRINGS EN PYTHON
Strings como Listas
"""
# split, genera una lista a partir de un string
courses = "Python, PHP, Rub,y Django, MongoDB, Ruby on Rails"
list_courses = courses.split(", ") # Devuelve una lista de strings en función de un separador el cual sea otro caracter o string
print(list_courses, type(list_courses), len(list_courses))

# join, genera una string a partir de un lista
list_courses2 = ["Python", "PHP", "Ruby", "Django", "MongoDB", "Ruby on Rails"]
courses2 = "--".join(list_courses2) # Devuelve un string a partir de una lista de strings 
print(courses2, type(courses2), len(courses2))

