'''2. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
    2.  Intente accesar a una variable global desde una función y cambiar su valor.'''

goodbye = 'Goodbye everyone'

def get_number():
    greet = 'Hello'
    num1 = int(input(f'{greet}, Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    addition(num1, num2)
    return num1, num2
    
def addition(num1, num2):
    result = num1 + num2
    global goodbye
    goodbye = 'Goodbye'
    print(f'{goodbye}, the result of the addition is: {result}')
    
get_number()