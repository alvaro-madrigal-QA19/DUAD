lista = [10,20,10,30,10,50,90,20,90,100,0,100]

print('MODO UNO')

valor_unico = 100
conteo = 0

for elemento in lista:
    if elemento == valor_unico:
        conteo +=1

print(conteo)        

print('*********************************')
print('MODO DOS') #

conteo = lista.count(10)  # Devuelve el número de veces que aparece 3 en la lista
print(conteo) 
