'''6. Cree una función que acepte un string con palabras separadas por un guión 
y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”'''
    
def get_words():
    chain_of_words = input('Enter the words separated by hyphens: ')
    
    words_list = chain_of_words.split('-')
    words_list.sort()
    result = '-'.join(words_list)
    print(f'Alphabetically ordered string: {result}')

get_words()