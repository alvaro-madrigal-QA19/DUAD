#1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
#y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def open_file():
#abrir archivo
    file = open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Files\\Listen_music.txt', 'r')
    contenido = file.readlines()  # Lee todo el archivo
    order_file(contenido)
    return contenido

def order_file(contenido):
    contenido.sort()
    for i in contenido:
        print(i)
    created_new_file(contenido)

def created_new_file(contenido):
#crear nuevo archivo
    with open("C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\Exercise_Files\\Files\\NEW_Listen_music.txt", "w") as file:
        for item in contenido:
         file.write(item + '\n')

open_file()