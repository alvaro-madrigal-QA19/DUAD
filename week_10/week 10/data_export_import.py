import csv
import os

def csv_export(list_students_data):

    with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 10\\students.csv', 'w', newline = '', encoding='utf-8') as file:
        columns = [
            'name','first_last_name','second_last_name','student_section','spanish_note'
                   ,'english_note','social_note','science_note'
                   ]

        write = csv.DictWriter(file, fieldnames=columns)
        write.writeheader()
    

        for x in list_students_data:
            write.writerow(x)

    print('Export completed successfully.')

def csv_import(list_students_data):

    if os.path.exists('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 10\\students_control\\students.csv'):
        
        with open('C:\\Users\\amugalde\\OneDrive - ASECCSS\\Personal\\Python\\Lyfter\\week 10\\students_control\\students.csv', 'r', newline = '', encoding='utf-8') as file:
       
            read = csv.DictReader(file)
            list_students_data.extend(read)
        print('Import completed successfully.')
    else:
        print('File does not exist')