'''Ejercicio 1: Leer y mostrar el contenido de un archivo
Crea un archivo de texto con algún contenido de tu elección (por ejemplo, un archivo llamado notas.txt).
Escribe un programa que abra ese archivo y muestre su contenido en la pantalla.'''

def open_file():
    file = open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\notas.txt', 'r')
               
    contenido = file.read()
    print(contenido)

open_file()

'''Ejercicio 2: Contar las líneas de un archivo
Crea un archivo de texto con varias líneas de texto (puedes usar el mismo archivo de la tarea anterior o uno nuevo).
Escribe un programa que cuente cuántas líneas tiene ese archivo.'''

def when_lines(archivo):
    with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\notas.txt', 'r') as file:
       line = file.readlines()
       return len(line)
    
archivo = 'C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\notas.txt'

numero_de_lineas = when_lines(archivo)
print(f"El archivo tiene {numero_de_lineas} líneas.")

'''Ejercicio 3: Escribir en un archivo
Crea un archivo de texto vacío llamado nuevo_archivo.txt.
Escribe un programa que abra ese archivo y le escriba tu nombre y la fecha actual en el archivo.'''

def write_file():
    try:
        with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\new_file.txt','w') as file:
            file.write('Mi nombre es Alvaro Madrigal')
            file.write('\nHoy es 17/03/2025')
    except FileNotFoundError:
        print('Archivo no encontrado:')
    try:    
        with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\new_file.txt','r') as file:   
            contenido = file.read()
            print(contenido)
    except FileNotFoundError:
        print('Archivo no encontrado:')
write_file()

'''Ejercicio 4: Agregar texto a un archivo existente
Crea un archivo de texto con alguna frase, por ejemplo, frases.txt.
Escribe un programa que agregue una nueva línea con otro texto al final de ese archivo sin borrar el contenido anterior.'''
def escribir():

    try:    
        with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\frases.txt','a') as file:
         file.write('\nGoku 6')
    except FileNotFoundError:
     print('Archivo no encontrado')
    try:            
        with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\frases.txt','r') as file:
         contenido = file.read()
         print(contenido)
    except FileNotFoundError:
     print('Archivo no encontrado')

escribir()

'''Ejercicio 5: Leer un archivo línea por línea
Crea un archivo de texto con varias líneas de texto.
Escribe un programa que lea el archivo línea por línea y las imprima por pantalla, pero mostrando solo las líneas que contengan 
la palabra "importante".'''

def importante():
   try: 
      with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\importante.txt','r') as file:
            for line in file:
                if "importante" in line:
                    print(line.strip())
   except FileNotFoundError:
      print('archivo no existe')            
        
importante()

'''Ejercicio 6: Copiar contenido de un archivo a otro
Crea dos archivos de texto (archivo_origen.txt y archivo_destino.txt).
Escribe un programa que copie el contenido de archivo_origen.txt a archivo_destino.txt.'''

def copiar_pegar():
    try:
        with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\archivoOrigen.txt', 'r') as file:
         contenido = file.readlines()
         print(contenido)

         

    except FileNotFoundError:
        print('archivo no existe')

    try: 
        with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\archivoDestino.txt', 'w') as file:
           for line in contenido:
                file.write(str(line.strip()+ '\n'))
          
    except FileNotFoundError:
        print('archivo no existe')  


copiar_pegar()

'''Ejercicio 7: Buscar una palabra en un archivo
Crea un archivo con algunas frases.
Escribe un programa que busque si una palabra específica (por ejemplo, "python") existe en el archivo. Si la palabra está presente,
imprímelo en pantalla.'''

def palabra_repetida():
    try:
        with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\importante.txt', 'r') as file:
            contenido = file.readlines()

        for line in contenido:
            if 'hoy' in line:
                print(line.strip()) 
    except FileNotFoundError:
        print('Archivo No econtrado')

palabra_repetida()

'''Ejercicio 8: Crear un archivo con números
Crea un archivo de texto llamado numeros.txt y escribe 10 números en él, uno por línea.
Escribe un programa que lea ese archivo y calcule la suma de esos números.'''

with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\numeros.txt', 'w') as file:
    for i in range(10):
        file.write(str(i).strip() + '\n')

with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\numeros.txt', 'r') as file:
    result = sum(int(line.strip()) for line in file)
    print(result)


'''Ejercicio 9: Eliminar contenido de un archivo
Crea un archivo con texto.
Escribe un programa que borre el contenido de ese archivo sin eliminar el archivo en sí.'''

with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Extras_Files\\frases.txt', 'w') as file:
    
    pass
print(file)

'''Ejercicio 10: Reemplazar texto en un archivo
Crea un archivo de texto con algunas frases.
Escribe un programa que busque una palabra o frase y la reemplace por otra dentro del archivo.'''