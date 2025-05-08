'''4. Cree un programa que elimine todos los números impares de una lista.
    1. Ejemplos:
    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`'''


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = []
lista3 = []

for i in lista:
    if i % 2 == 0 :
        lista2.append(i)
    else:
        lista3.append(i)

print(f'La lista par es: {lista2}, \nLa lista impar es: {lista3}')

