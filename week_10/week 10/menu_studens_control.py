

from actions_menu import add_students, show_all_students, best_average, see_note_average
from data_export_import import csv_export, csv_import

def option_menu():
    students_list = []
    print('\n\033[92m**** Welcome to Control Students ****\033[0m')
    while True:
        print('\n\033[92m1.\033[0m Add Student(s)')
        print('\033[92m2.\033[0m Show All Students Information')
        print('\033[92m3.\033[0m Show Student Information by ID')
        print('\033[92m4.\033[0m Show Top 3 Students by Average')
        print('\033[92m5.\033[0m Show average for All Students')
        print('\033[92m6.\033[0m Export Data to CSV')
        print('\033[92m7.\033[0m Import Data from CSV')
        print('\033[92m8.\033[0m Exit\n')

        try:
            option = input('Please, enter an option: ')

            if option not in ['1', '2', '3', '4', '5', '6', '7', '8']:
                print('\n***Invalid option. Please enter a valid option (1, 2, 3, 4, 5, 6, 7 , 8)***\n')
                continue

            if option == '1':
                students_list = add_students(students_list)
                students_list = continue_add(students_list)

            if option == '2':
                show_all_students(students_list)
                

            if option == '3':
                print('opcion 3')

            if option == '4':
                best_average(students_list)

            if option == '5':
                see_note_average(students_list)

            if option == '6':
                csv_export(students_list)

            if option == '7':
                csv_import(students_list)

            if option == '8':
                print('*** Goodbye ***')
                break

        except ValueError as e:
            print(f'\n\033[93mPlease, enter the correct number. {e}\033[0m\n')

def continue_add(list_students_data):
    continue_progress = input('Do you want to continue adding students? (yes/no)').strip().lower()
    if continue_progress == 'yes':
        list_students_data = add_students(list_students_data)
        return list_students_data
    return list_students_data


