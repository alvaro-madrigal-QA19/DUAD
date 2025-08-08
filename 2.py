'''2. Cree una clase de `Bus` con:
    1. Un atributo de `max_passengers`.
    2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). 
    **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.

    3. Un método para bajar pasajeros uno por uno (en cualquier orden).'''
class Person():
    def __init__(self, name):
        self.name = name

class Bus:
    
    def __init__(self, max_passengers=1): 
        self.max_passengers = max_passengers
        self.add_passenger_list = []
        

    def add_passengers(self, person):
        if len(self.add_passenger_list) == self.max_passengers:
            print(f"Sorry, you can't go up the bus, maximum capacity is {self.max_passengers} and it is already full" )
        else:
            self.add_passenger_list.append(person)
            for i in self.add_passenger_list:
                print(f'- {i.name}')    
        
    def drop_off_passengers(self):
        self.add_passenger_list.pop()
        for i in self.add_passenger_list:
                print(f'- {i.name}')

bus = Bus(max_passengers=2) 

while True:
    print('\n1.Add Person of the Bus.')
    print('2.Drop off passengers.')
    print('3.Exit.')

    option = int(input('Please choose one: '))

    if option == 1:
        passenger = input('Please enter the name: ')
        person = Person(passenger)
        bus.add_passengers(person) 
        
    elif option == 2:
        bus.drop_off_passengers()

    else:
        print('\nThanks')
        break