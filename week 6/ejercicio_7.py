'''7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]'''
numbers_list = [1, 4, 6, 7, 13, 9, 67]

#es primo o no
def is_prime(num):
    if num <= 1:
        return False 
    for i in range(2, num): 
        if num % i == 0: 
            return False
    return True 


def get_prime(numbers_list):
    prime_numbers = [] 
    for number in numbers_list:
        if is_prime(number): 
            prime_numbers.append(number)  
    return prime_numbers 


result = get_prime(numbers_list)
print(f'The prime numbers are: {result}')