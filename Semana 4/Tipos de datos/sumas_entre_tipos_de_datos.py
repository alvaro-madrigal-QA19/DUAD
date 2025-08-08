#1. string + string → ?
num1 = '5'
num2 = '70'

entero1 = int(num1)
entero2 = int(num2)

suma = entero1 + entero2
print(f'La suma entre 2 STRING es: {str(suma)}')

#2. string + int → ?
num3 = '5'
num4 = 90
entero3 = int(num3)

suma2 = entero3 + num4
print(f'La suma entre STRING y INT es: ***{str(suma2)}***')


#3. int + string → ?
num5 = 5
num6 = '105'
entero4 = int(num6)

suma3= entero4 + num5
print(f'La suma INT y STRING es: ***{str(suma3)}***')

#4. list + list → ?
lista1 = [1,2,3]
lista2 = [3,2,7]

suma4 = lista1[1] + lista2[1]
print(f'La suma entre campos especificos de LISTA es: ***{suma4}***')

suma_listas1 = sum(lista1)
print(f'La suma todos los valores de LISTA es: ***{suma_listas1}***')

suma_listas2 = sum(lista2)
print(f'La suma todos los valores de LISTA es: ***{suma_listas2}***')


#5. string + list → ?
lista3 = [10,10,5]
cadena = '5'

entero5 = int(cadena)
suma5 = entero5 + lista3[2]
print(f'La suma de LISTA y STRING es: ***{suma5}***')



#6. float + int → ?
flotante = 3.80
numero_entero = 50
suma_entero_flotante = flotante + numero_entero
print(f'La suma de FLOTANTE y INT es: ***{suma_entero_flotante}***')


#7. bool + bool → ?
booleano1 = True
booleano2 = False

operacion1 = booleano1 or booleano2
print(f'La operacion de suma de BOOLEANOS es: ***{operacion1}***')

operacion2 = booleano1 and booleano2
print(f'La operacion de suma de BOOLEANOS es: ***{operacion2}***')