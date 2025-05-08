'''3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
    1. Ejemplos:
    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`'''


lista = [4, 3, 6, 1, 7]

num1 = lista.pop(0)
num2 = lista.pop()

lista.append(num1)   
lista.insert(0, num2) 

print(lista)

