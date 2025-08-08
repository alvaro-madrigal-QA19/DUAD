'''2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
    1. Pista: investigue de que otras maneras se puede usar el `range`.
    2. Ejemplos:
    3. `my_string = ‘Pizza con piña’` → 
    a
    ñ
    i
    p
    
    n
    o
    c
    
    a
    z
    z
    i
    p'''

'''
>> reversed: se utiliza para mostrar los datos de izquierda a derecha
'''
my_string1 = 'Pizza con piña'
print('\n#1')
for i in reversed(my_string1):
    print(i)

'''
>> len(my_string2) nos da la longitud de la cadena, 14, y se almacen en variable
>> range(longitud) toma el indice Indice 14.
>> my_string2[longitud-n-1] toma la longitud, cada vuelta le resta un numero iniciando desde el final de la cadena

'''
my_string2 = 'Arroz con coco'
longitud = len(my_string2)
print('\n#2')
for n in range(longitud):
    print(my_string2[longitud-n-1])


'''
>> len(my_string3) nos da la longitud de la cadena, 14
>> len(my_string) - 1 nos da el índice del último carácter de la cadena. Indice 13.
>> -1 especifica el índice del primer carácter de la cadena. En Python, el índice -1 se refiere al último elemento de una secuencia.
>> el tercer -1 indica un paso negativo, la iteración se realizará de manera decreciente, desde el último carácter hasta el primero.
'''
my_string3 = 'Salsa con Coco'
print('\n#3')
for z in range(len(my_string3) -1 ,-1, -1):
    print(my_string3[z])