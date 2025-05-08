'''4. Cree un programa que elimine todos los números impares de una lista.
    1. Ejemplos:
    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`'''

my_list = [1,2,3,4,5,6,7,8,9,10]
nueva_lista = []

for i in my_list:

    if i % 2 == 0:
        nueva_lista.append(i)

print(nueva_lista)
