lista = [20,20,20,10,50,5,66666,10,1]

lista2 =  []


print('MODO UNO')
for i in lista:
    if i not in lista2:
        lista2.append(i)

print(lista2)


print('*********************************')
print('MODO DOS') #este modo no lo tira en orden

lista2 = list(set(lista))
print(lista2)