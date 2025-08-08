'''3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
    1. Ejemplos:
    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`'''


my_list = [20,0,4, 3, 6, 1, 7, 10, 40, 50, 70]

elimnar_primero = my_list.pop(0) #elimina el primer valor
eliminar_ultimo = my_list.pop() #elimina el ultimo valor

my_list.insert(0, eliminar_ultimo) #se inserta en la posicion 0 el ULTIMO valor eliminado de la lista
my_list.append(elimnar_primero) #se inseta en la primer posicion el PRIMER valor eliminado 
print(my_list)
