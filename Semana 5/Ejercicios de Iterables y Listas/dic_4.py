print('Bienvenido al sistema de registro')

#Lista donde se almacena todo 
mi_list = []


while(True):

    fecha = str(input('Agregue una fecha: '))
    email = str(input('Ingrese email: '))

    #Lista donde se almacena las caracteristicas del producto
    item_list = []

    while(True):
    
        name = str(input('Agregue nombre del producto: '))
        upc = str(input(f'Agregue código del producto "{name}": '))
        unit_price = int(input(f'Agregue el precio del producto "{name}": $'))

        #se agregan a la lista de items
        item_list.append({'name' : name, 'upc' : upc, 'unit_price' : unit_price})
       
        #Se consulta si desea agregar mas productos a la lista de diccionarios
        option1 = input('Deseas agregar otro producto? S/N: ')
        if option1 != 'S':
            break

    #Se agregar los datos a la lista 
    mi_list.append({'fecha' : fecha, 'email' : email, 'items' : item_list})

    #Se consulta si desea agregar mas productos a la lista 
    option2 = input('Deseas REGISTRAR otra venta? S/N: ')
    if option2 != 'S':
        break

total_ventas = {}

for venta in mi_list:
    # Iterar sobre cada ítem en la venta
    for item in venta['items']:
        # Obtener el UPC y el precio unitario del ítem
        upc = item['upc']
        precio_unitario = item['unit_price']
        # Actualizar el total de ventas del UPC en el diccionario
        if upc in total_ventas:
            total_ventas[upc] += precio_unitario
        else:
            total_ventas[upc] = precio_unitario

print(total_ventas)





