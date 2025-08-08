'''Cree un programa que le pida al usuario su nombre, apellido, y edad, 
y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.'''


name = str(input('Por favor ingrese su nomnbre: '))
last_name = str(input('Por favor ingrese su apellido: ')) 
age = int(input('Por favor ingrese su edad: ')) 

if (age <= 2):
    print(f'Usted {name} {last_name} es un/una bebé')
elif(age <=12):
    print(f'Usted {name} {last_name}  es un/una preadolescente')
elif(age <=18):
    print(f'Usted {name} {last_name}  es un/una adolecente')
elif(age <=35):
    print(f'Usted {name} {last_name}  es un/una adulto/a joven')
elif(age <=60):
    print(f'Usted {name} {last_name}  es un/una adulto/a')
elif(age >=61):
    print(f'Usted {name} {last_name}  es un/una adulto/a mayor')

