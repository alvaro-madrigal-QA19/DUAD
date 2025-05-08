'''5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
    1. Ejemplos:
    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.'''

contador = 1
lista = []

'''while(contador <= 10):
    numero = int(input(f'Agregue el numero #{contador}: '))
    lista.append(numero)
    contador += 1'''

for i in range(0,10):
    numero = int(input(f'Agregue el numero #{contador}: '))
    lista.append(numero)
    contador += 1

print(f'Los valores de la lista son: {lista}, \nEl numero mayor es {max(lista)}')