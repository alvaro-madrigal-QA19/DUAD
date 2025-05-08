lista = []

cant = int(input('Ingrese la cantidad de numeros que va registrar: '))
contador = 1

while(contador <= cant):
    num = int(input(f'Ingrese el valor #{contador}: '))
    lista.append(num)
    contador += 1

print(lista)
print('DATOS EN REVERSA: ')
for i in range(len(lista)-1,-1,-1):
    print(lista[i])
