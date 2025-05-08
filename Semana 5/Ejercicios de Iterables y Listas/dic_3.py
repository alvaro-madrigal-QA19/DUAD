'''3. Cree un programa que use una lista para eliminar keys de un diccionario.
    1. Ejemplos:
    2. `list_of_keys = [’access_level’, ‘age’]`
    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`'''

list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
    #{'name': 'John', 'email': 'john@ecorp.com'}

#for i in employee.items():
#    print(i)

#mediante if
if list_of_keys[0] in employee:
    del employee[list_of_keys[0]]
if list_of_keys[1] in employee:
    del employee[list_of_keys[1]]       
print(employee)

#mediante ciclo for
for key in list_of_keys:
    if key in employee:
        del employee[key]
print(employee)
