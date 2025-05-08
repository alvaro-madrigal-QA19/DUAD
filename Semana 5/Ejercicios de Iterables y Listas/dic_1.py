'''Cree un diccionario que guarde la siguiente información sobre un hotel:
nombre
numero_de_estrellas
habitaciones
El key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
numero
piso
precio_por_noche'''

print('Bienvenido al sistema ***INICIANDO REGISTRO***')

#se crea el diccionario vacio
hotel_information = {}

#se SOLICITAN los datos del diccionario
name = str(input('Ingrese el nombre del Hotel: '))
star = int(input(f'Ingrese la cantidad de estrellas que tiene el hotel ***{name}***: '))
rooms = int(input(f'Ingrese la cantidad de habitaciones que tiene el hotel ***{name}***: '))

#se agregan los datos al diccionario
hotel_information['nombre_hotel'] = name
hotel_information['cant_estrellas'] = star
hotel_information['cant_habitaciones'] = rooms


#se crea un ciclo para agregar y crear los datos relacionados a las habitaciones
counter = 1
while(counter <= rooms):
    num_room = int(input(f'Ingrese el código identificador de la habitación #{counter}: '))
    floor = int(input(f'Ingrese el piso donde se encuentra la habitación #{counter}: '))
    price_night = float(input(f'Ingrese el precio de la habitación #{counter}: $'))
    hotel_information[f'room{counter}'] = num_room,floor,price_night
    counter += 1

#se imprimen los datos del diccionario
print('\n***************\n')
for keys, values in hotel_information.items():
    print(f'{keys} >>> {values}')

#se imprime ciertos datos del diccionario
print('\n***************\n')
print(hotel_information.get('nombre_hotel'))
print(hotel_information.get('cant_estrellas'))
print(hotel_information.get('cant_habitaciones'))

#se imprime el diccionario completo
print('\n***************\n')
print(hotel_information)