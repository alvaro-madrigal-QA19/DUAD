diccionario = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Claves que deseas incluir en la suma
claves_a_sumar = ['a', 'c']

# Sumar los valores correspondientes a las claves específicas
suma = sum(diccionario[clave] for clave in claves_a_sumar)

# Mostrar la suma
print("La suma de los valores específicos del diccionario es:", suma)