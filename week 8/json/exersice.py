import json

pokemon = [
  {
    "name": {
      "english": "Pikachu"
    },
    "type": [
      "Electric"
    ],
    "base": {
      "HP": 35,
      "Attack": 55,
      "Defense": 40,
      "Sp. Attack": 50,
      "Sp. Defense": 50,
      "Speed": 90
    }
  },
  {
    "name": {
      "english": "Charmander"
    },
    "type": [
      "Fire"
    ],
    "base": {
      "HP": 39,
      "Attack": 52,
      "Defense": 43,
      "Sp. Attack": 60,
      "Sp. Defense": 50,
      "Speed": 65
    }
  },
  {
    "name": {
      "english": "Squirtle"
    },
    "type": [
      "Water"
    ],
    "base": {
      "HP": 44,
      "Attack": 48,
      "Defense": 65,
      "Sp. Attack": 50,
      "Sp. Defense": 64,
      "Speed": 43
    }
  }
]




def create_file():
    try:
        with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 8\\json\\test.json','w') as file:
            enter_features_pokemon()
            json.dump(pokemon, file, indent=4)
    except FileNotFoundError:
            print('File not Found')



def enter_features_pokemon():
    try:
        amount_pokemon = int(input('How many Pokemon would you like to add?: '))
        
    
        count = 1
        for i in range(amount_pokemon):
                while True:
                    name_pokemon = input(f'Enter name of pokemon #{count}: ')
                    if not name_pokemon.strip():
                        print('Please, enter the correct name.')
                    else:
                         break
                while True:
                    type_pokemon = input(f'Enter type of pokemon #{count}: ')
                    if not type_pokemon.strip():
                         print('Please, enter the correct type.')
                    else:
                         break
                count +=1    
                try:

                    hp = int(input('Enter HP of pokemon: '))
                    attack_pokemon = int(input('Enter Attack of pokemon: '))
                    defense_pokemon = int(input('Enter Defense of pokemon: '))
                    sp_attack_pokemon = int(input('Enter Sp. Attack of pokemon: '))
                    sp_defense_pokemon = int(input('Enter Sp. Defense of pokemon: '))
                    speed_pokemon= int(input('Enter speed of pokemon: '))

                except ValueError as e:
                    print('This Pokemon was not added to the list')
                    print(f'Invalid Value: {e}')
                    continue
                
                data_of_pokemon = {}
                types_pokemon = []
                features_of_pokemon = {}

                data_of_pokemon['name'] = {'english' : name_pokemon}
                types_pokemon.append(type_pokemon)
                data_of_pokemon['type'] = types_pokemon
                features_of_pokemon['HP'] = hp
                features_of_pokemon['Attack'] = attack_pokemon
                features_of_pokemon['Defense'] = defense_pokemon
                features_of_pokemon['Sp. Attack'] = sp_attack_pokemon
                features_of_pokemon['Sp. Defense'] = sp_defense_pokemon
                features_of_pokemon['Speed'] = speed_pokemon
                data_of_pokemon['base'] = features_of_pokemon

                pokemon.append(data_of_pokemon) 
                

    except ValueError as e:
        print(f'Invalid Value: {e}')
    
    except FileNotFoundError:
        print('File Not Found')


create_file()        