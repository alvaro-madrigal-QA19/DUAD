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
    p

'''

cadena = 'Pizza con piña'

for i in range(len(cadena) -1,-1,-1):
    print(cadena[i])

#toma el largo de la cadena y lo va contando 1 a 1 para atras
