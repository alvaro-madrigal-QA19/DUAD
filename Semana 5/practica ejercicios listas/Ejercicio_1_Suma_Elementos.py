#Tienes una lista de números, calcula la suma de todos sus elementos.

lista = []
cant_numeros = int(input('Indique la cantidad de numeros a ingresar: '))

contador = 1

while(contador <= cant_numeros):
    num = int(input(f'Ingrese el valor #{contador}: '))
    lista.append(num)
    contador +=1

resultado = sum(lista)

print(f'La suma de todos los valores de la lista es: {resultado}')
