import re

def valid_name(field_name):
 while True:    
        try:
            names = str(input(f'-Please enter the {field_name}: '))

            value = r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$'
            

            if re.match(value, names) and names != "":
                return names
            else:
                print('\n\033[91mThe name must contain only letters.\033[0m\n')
                
        except ValueError:
            print(f'\n\033[93mPlease, Enter of valid {field_name}.\033[0m\n')

def valid_note(subject):

    while True:  
        try:
            note = float(input(f'-Please enter the {subject} note: '))
            if 0 <= note <= 100:
                return note
            else:
                print('\n\033[91mThe grade must be between 0 and 100\033[0m\n')
        except ValueError:
            print('\033[93mPlease, Enter of valid number.\033[0m\n')


def add_students(list_students_data):
    
    if list_students_data is None:
        list_students_data = []
    amount_studens = 0  
    counter = 1

    amount_studens = input('\nPlease enter the amount the students: ')

    for i in range(int(amount_studens)):
       
        dic_students_data = {}
      
        print(f'Student Data {counter}')
        name = valid_name('Name')
        first_last_name = valid_name('First Last Name')
        second_last_name = valid_name('Second Last Name')
        student_section = input('-Please enter the student section: ')
        spanish_note = valid_note('Spanish')
        english_note = valid_note('English')
        social_note = valid_note('Social')
        science_note = valid_note('Science')
        
        dic_students_data['name'] = name
        dic_students_data['first_last_name'] = first_last_name
        dic_students_data['second_last_name'] = second_last_name
        dic_students_data['student_section'] = student_section
        dic_students_data['spanish_note'] = spanish_note
        dic_students_data['english_note'] = english_note
        dic_students_data['social_note'] = social_note
        dic_students_data['science_note'] = science_note
        counter += 1
        
        list_students_data.append(dic_students_data)
    return list_students_data
    


def show_all_students(list_students_data):
    
    if not list_students_data :
        print("\nThere is no student data yet")
    else:    
        counter = 1
        for i in (list_students_data):
            print(f'\nStudent data {counter}\n')
        
            for clave in i:
                print(clave, ':', i[clave])

            counter +=1    

def best_average(list_students_data):
    list_average = []

    
    for i in list_students_data:
        suma = (i['spanish_note'] + i['english_note'] + i['social_note'] + i['science_note']) / 4
        dicct_average = {}

        dicct_average = {
            'name': i['name'],
            'average': suma
        }
        list_average.append(dicct_average)
    
    estudiantes_ordenados = sorted(
        list_average, 
        key=lambda average: average['average'],  
        reverse=True   
        )

    for items, values in enumerate(estudiantes_ordenados[:3], 1):
        nombre = values['name']
        average = values['average']
        print(f"{nombre}: {average:.2f} average")

    return estudiantes_ordenados


def see_note_average(list_students_data): 
    list_averages = []

    for i in list_students_data:
        suma = (i['spanish_note'] + i['english_note'] + i['social_note'] + i['science_note']) / 4
        dicct_averages = {}  
        dicct_averages = {
            'name': i['name'],
            'average': suma
        }
        list_averages.append(dicct_averages)
    sumar = 0
    for i in list_averages:
        sumar += (i['average']) 
        
    total_average = sumar / len(list_averages)
        

    for items, values in enumerate(list_averages, 1):
        nombre = values['name']
        average = values['average']
        print(f"{nombre}: {average:.2f} average")
    print(f'total average: {total_average}')


