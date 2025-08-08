'''2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
    1. Ejemplos:
    2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
    `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
    → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}'''

list_1 = ['first_name', 'last_name', 'role'] 

#se crea la LISTA #2 vacia
lista_2 = []

#se crea el diccionario vacio
information_dicc = {}

#se solicitan los datos para llenar la LISTA #2
print('Bienvenido al sistema ***LLENADO DE LISTA #2***')
first_name = str(input('Digite su nombre: '))
last_name = str(input(f'Por favor {first_name}, digite su apellido: '))
role = str(input(f'Por favor {first_name} {last_name}, digite su profesion: '))

#Se agregan los datos a la lista
lista_2.append(first_name)
lista_2.append(last_name)
lista_2.append(role)


#Se agregan los datos al diccionario
information_dicc[list_1[0]] = lista_2[0] 
information_dicc[list_1[1]] = lista_2[1] 
information_dicc[list_1[2]] = lista_2[2] 

#se unen las dos listas y se imprimen los valores del diccionario
print('\n***************\n')
for indice_lista2, valor_lista1 in enumerate(list_1): 
    print(f'{valor_lista1}: {lista_2[indice_lista2]}')


#se imprime el diccionario
print('\n***************\n')
print(information_dicc)

