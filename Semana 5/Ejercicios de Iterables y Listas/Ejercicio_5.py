'''5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, 
seguido del numero ingresado más alto.
    1. Ejemplos:
    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.'''

contador = 1
lista = []

while(contador <= 10):
    numero = int(input(f'Ingrese el numero {contador}: '))
    lista.append(numero)
    contador +=1
   
print(f'Los números de la lista son: {lista} 
      \nEl número mayor de la lista es: *** {max(lista)} ***')



