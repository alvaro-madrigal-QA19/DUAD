'''5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”'''

phrase = 'I love Nación Sushi'

def uppercase_lowercase():
    countUppercase = 0
    countLowercase = 0
    for i in phrase:
        if i.isupper():
            countUppercase +=1
        if i.islower():
            countLowercase +=1
    print(f'The letter uppercase are: {countUppercase}, The letter lowercase are: {countLowercase}')


uppercase_lowercase()