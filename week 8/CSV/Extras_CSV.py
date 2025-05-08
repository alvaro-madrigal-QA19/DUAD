'''Ejercicio 1: Leer un archivo CSV
Objetivo: Leer un archivo CSV que contenga información sobre productos (por ejemplo: nombre, precio y cantidad) y mostrar el contenido de cada fila en la consola.
Instrucciones:
Crea un archivo CSV llamado productos.csv con las siguientes columnas: nombre, precio, cantidad.
Usa el módulo csv de Python para abrir y leer el archivo.
Muestra cada fila del archivo en la consola.'''

import csv

data = [
    ['nombre', 'precio', 'cantidad'],
    ['Alvaro', '500', '7']
]

def productos():
    with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\CSV\\CSV_FILE\\test.csv', mode='w', newline='') as file:
        write_csv = csv.writer(file)
        write_csv.writerows(data)

    with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\CSV\\CSV_FILE\\test.csv', mode='r', newline='') as file:
        read_csv = csv.reader(file)

        for i in read_csv:
            print(i)
#productos()
'''Ejercicio 2: Escribir en un archivo CSV
Objetivo: Crear un nuevo archivo CSV con una lista de contactos.
Instrucciones:
Crea una lista de diccionarios con información de contactos, donde cada diccionario contiene nombre, email y teléfono.
Usa el módulo csv para crear un archivo llamado contactos.csv y escribir esta lista en el archivo.'''

contact_header = ['Nombre', 'Email', 'Telefono']

contact_data = []
def write_of_csv():

        amount_contact = int(input('Please enter amount contact: '))
        for i in range(amount_contact):
            name = input('Please, enter the name: ')
            email = input('Please, enter the email: ').lower()
            telefono = input('Please, enter the phone number: ')

            persona = {
                'Nombre' : name,
                'Email' : email,
                'Telefono' : telefono
            }
            contact_data.append(persona)

        with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\CSV\\CSV_FILE\\contactos.csv', mode= 'w', newline= '') as file:
            escritor = csv.DictWriter(file, fieldnames= contact_header) 
            escritor.writeheader()   
            escritor.writerows(contact_data)


write_of_csv()




'''Ejercicio 3: Modificar datos en un CSV
Objetivo: Leer un archivo CSV, modificar algunos valores y guardar los cambios en un nuevo archivo.
Instrucciones:
Usa el archivo productos.csv creado en el ejercicio 1.
Incrementa en un 10% el precio de todos los productos.
Guarda el archivo modificado con un nuevo nombre, como productos_actualizados.csv.'''


'''Ejercicio 4: Filtrar datos de un CSV
Objetivo: Leer un archivo CSV y filtrar filas basadas en una condición específica.
Instrucciones:
Usa el archivo productos.csv y filtra solo los productos cuyo precio sea mayor a 50.
Muestra en la consola solo el nombre y el precio de esos productos.'''



'''Ejercicio 5: Calcular estadísticas a partir de un CSV
Objetivo: Calcular el total de ventas en función de la cantidad y el precio de los productos.
Instrucciones:
Usa el archivo productos.csv y calcula el total de ventas para cada producto, multiplicando el precio por la cantidad disponible.
Muestra el total de ventas para cada producto en la consola.'''