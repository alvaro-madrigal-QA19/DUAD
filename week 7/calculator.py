'''Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. 
El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.'''

current_value = 0
print('Welcome to Calculator')
print(f'The current value is: {current_value}')
def menu():
 
    while True:
        print('\n1. Subtraction ')
        print('2. Addition ')
        print('3. Multiply ')
        print('4. Division ')
        print('5. Exit')
        
        try:
            
            option = input('Please, enter an option: ')
            
            if option not in ['1', '2', '3', '4', '5']:
                print('Invalid option. Please enter a valid option (1, 2, 3, 4, 5).')
                continue  # Si no es una opción válida, se vuelve a pedir la opción
     
            
            if option == '1':
                result = Subtraction()
                
                
            elif option == '2':
                result = Addition()
                
                
            elif option == '3':
               result = multiplication()
                
            
            elif option == '4':
                result = division()
                
            elif option == '5':
                print('Goodbye')
                break
            
        except ValueError:
            print('Please, enter the correct number: ')
        
def Subtraction():
    result = None
    global current_value
    
    try:
        num1 = float(input('Enter your number: '))
        
        result = current_value - num1
        print(f'This is the result of subtraction: {result}')
        
        current_value = result
        print(f'Update value: {current_value}')
        
    except ValueError as e:
        print(f'This is invalid format! {e}')    
    
    return result
    
    
    
def Addition():
    result = None
    global current_value
    
    try: 
        num1 = float(input('Enter your number: '))
        
        result = current_value + num1
        print(f'This is result of addition: {result}')
    
        current_value = result
        print(f'Update value: {current_value}')
    
    except ValueError as e:
        print(f'This is invalid format! {e}')
    
    return result
    
def multiplication():
    result = None #esto es para que la ecepcion siempre detecte un valor
    global current_value
    
    try: 
        num1 = float(input('Enter your number: '))
        
        result = current_value * num1
        print(f'This is result of Multiply: {result}')
        
        current_value = result
        print(f'Update value: {current_value}')
        
    except ValueError as e:
        print(f'This number is invalid format! {e}')
        
    return result
    
def division():
    result = None
    global current_value
    
    try:
        num1 = float(input('Enter your number: '))
        
        result = current_value / num1
        print(f'This is a result of the division: {result}')
        
        current_value = result
        print(f'Update value: {current_value}')
        
    except ValueError as e:
        print(f'This number is invalid format! {e}')
        
    except ZeroDivisionError as e:
        print(f'Cannot divide by zero. {e}')

menu()