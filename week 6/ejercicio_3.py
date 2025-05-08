'''3. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41'''
    
number_list = []

def get_number():
    add_numbers = int(input('Enter the amount of numbers to add to the list: '))
    
    for y in range(add_numbers):
        value = int(input('Add a number: '))
        number_list.append(value)

    return_list(number_list)   

def return_list(number_list):
    for i in number_list:
        total = sum(number_list)
    print(f'The result of the addition is: {total}')
    
get_number()