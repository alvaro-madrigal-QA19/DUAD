'''1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
    1. Ejemplos:
    2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
    `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
    Hay casos
    en los
    que la
    iteracion por
    indice es
    muy util'''

first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util'] 

for indice_lista2, valor_lista1 in enumerate(first_list): 
    print(valor_lista1, second_list[indice_lista2])


'''
enumerate >>> funciona para acceder al indice como al valor de cada indice
linea 15 >>> se crean dos variables para capturar el indice y el valor de la lista
linea 16 >>> se muestra valores de la lista1 y los datos de la lista2
'''