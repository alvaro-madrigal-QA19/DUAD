# Inicializamos una variable para contar cuántos números se han ingresado
contador = 0

# Inicializamos una variable para almacenar el mayor número ingresado
mayor = float('-inf')  # Inicializamos con el menor valor posible de un float

# Mientras no se hayan ingresado tres números
while contador < 3:
    # Pedimos al usuario que ingrese un número
    numero = float(input("Ingrese un número: "))
    
    # Verificamos si el número ingresado es mayor que el actual mayor número
    if numero > mayor:
        mayor = numero  # Actualizamos el mayor número
        
    # Incrementamos el contador de números ingresados
    contador += 1

# Mostramos el mayor número ingresado
print("El mayor número ingresado es:", mayor)