# Crear una lista vacía de ventas
ventas = []

# Solicitar datos de ventas al usuario
while True:
    # Ingresar datos de la venta
    date = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
    customer_email = input("Ingrese el correo electrónico del cliente: ")
    
    # Crear una lista de items para esta venta
    items = []
    while True:
        # Ingresar datos del item
        name = input("Ingrese el nombre del producto: ")
        upc = input("Ingrese el código UPC del producto: ")
        unit_price = float(input("Ingrese el precio unitario del producto: "))
        
        # Agregar el item a la lista de items
        items.append({"name": name, "upc": upc, "unit_price": unit_price})
        
        # Preguntar al usuario si desea agregar otro producto a esta venta
        agregar_otro = input("¿Desea agregar otro producto a esta venta? (s/n): ")
        if agregar_otro.lower() != "s":
            break
    
    # Agregar los datos de la venta a la lista de ventas
    ventas.append({"date": date, "customer_email": customer_email, "items": items})
    
    # Preguntar al usuario si desea ingresar otra venta
    agregar_otra_venta = input("¿Desea ingresar otra venta? (s/n): ")
    if agregar_otra_venta.lower() != "s":
        break

# Imprimir la lista de ventas para verificar
print(ventas)
