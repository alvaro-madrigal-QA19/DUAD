print('Bienvenido')

lista_1 = []

while(True):
    date = str(input('Digite la fecha(DD/MM/AAAA): '))
    email = str(input('Digite su email(dominio@dominio.com): '))

    lista_1.append({"fecha" : date})

    items = []
    while(True):
        []
        name = str(input('Digite el nombre del producto: '))
        upc = str(input(f'Digite el código del producto "{name}: '))
        unit_price = float(input(f'Digite el precio del producto "{name}: $'))

dic_2({"nombre" : name, "upc" : upc, "precio_producto" : unit_price})