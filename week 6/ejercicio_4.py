'''4. Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”'''
def get_word():
    word = input('Enter a word: ')
    print_reversed_word(word)

def print_reversed_word(word):
    for i in range(len(word)-1,-1,-1):
        print(word[i], end="")
        
get_word()   