'''Cree un programa con un numero secreto del 1 al 10. 
El programa no debe cerrarse hasta que el usuario adivine el numero.'''

import random
secret_num = random.randint(1,10) #se implementa el random.randint para el rango de numeros

while(True):

    number = int(input('Por favor ingrese un número del 1 al 10: '))

    if(number == 1 or number <= 10):
        if(number==secret_num):
            print(f'Felicidades adivino el número secreto: {secret_num}.')
            break
        else:
            print(f'El {number} no es número secreto.')
    else:
        print(f'El número {number} esta fuera del rango.')