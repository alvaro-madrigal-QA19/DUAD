'''2. Lea sobre el resto de métodos del módulo `csv` [aqui](https://docs.python.org/es/3/library/csv.html) 
y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por *tabulaciones* en vez de por *comas*.
    1. Ejemplo de archivo final:
        
       
        nombre	genero	desarrollador	clasificacion
        Grand Theft Auto IV	Accion	Rockstar Games	M
        The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
        Tony Hawk's Pro Skater 2	Deportes	Activision	T
        '''

import csv

#nombre de columnas del csv
game_header = (
        'name',
        'genre',
        'developer',
        'classification'
    ) 


def enter_amount_games():
    amount_games = int(input('Please, enter the number of games: '))#cantidad de juegos a agregar
    
    games = [] #lista para agregar los diccionarios
    
    for i in range(amount_games):
        
        game_data = {} #diccionarios que se agregaran a la lista

        name = input('Please, enter the name of game: ')
        genre = input("Please, enter the genre of game: ")
        developer = input('Please, enter the video game developer: ')
        clasification = input('Please, enter the classification of the game: ')
    
        #se agregan al diccionario
        game_data['name'] = name
        game_data['genre'] = genre
        game_data['developer'] = developer
        game_data['classification'] = clasification
    
        games.append(game_data) #se agrega el diccionario a la lista

    write_to_csv(games, game_header) #se manda a llamar a la funcion y se le pasa la lista de dicc y las columnas
    print(games)

def write_to_csv(games, game_header):

    with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\CSV\\CSV_FILE\\games2.txt', mode='w', newline = '', encoding='utf-8') as file:  
        escritor = csv.DictWriter(file, game_header, delimiter = '\t') #file = archivo que se trabajara / #game_header es la tupla que son las columnas
        escritor.writeheader() #se le escribe al archivo las columnas
        escritor.writerows(games) #se le escribe los demas datos y se le pasa variable

    
enter_amount_games()