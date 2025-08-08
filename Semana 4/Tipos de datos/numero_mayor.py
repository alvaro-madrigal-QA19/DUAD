'''Cree un programa que le pida tres números al usuario y muestre el mayor.'''


num = float(input('Ingrese el número '))
mayor = num 

contador = 1

while(contador <= 2):
    num2 = float(input('Ingrese otro número: '))
    
    if(num2 > mayor):
        mayor = num2        
    contador = contador + 1  
else:
    print(f'El número mayor es: **** {mayor} ****')
