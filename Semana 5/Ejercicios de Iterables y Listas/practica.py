## Iteración directa
list_artistas = [
    'Franco de vita',
    'Jose Jose',
    'Eros Ramazzotti',
    'Eros Ramazzotti',
    'Eros Ramazzotti',
    'Eros Ramazzotti'
]

for artistas in list_artistas:
    if artistas ==  'Eros Ramazzotti':
        print(f'El mejor es Eros Ramazzotti')
    else:
        print(f'Mi artista favorito es: {artistas}')



## Iteración por indice
list_artistas1 = [
    'Franco de vita',
    'Jose Jose',
    'Eros Ramazzotti'
]

for index in range(0,len(list_artistas1)):
    record = list_artistas1[index] # se le asigna la cantidad de elementos de la lista (0,1,2)
    print(f'Record {index}: {record}') # imprime la cantidad con el nombre del elemento

    
