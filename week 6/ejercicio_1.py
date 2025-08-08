'''1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.'''
def greet():
    print('Hello')
    goodbye()
    
def goodbye():
    print('bye')
    
greet()