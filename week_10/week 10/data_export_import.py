import csv
import os

def csv_export(list_students_data):

    with open('C:\\Users\\pc\\Desktop\\Alvaro\\Lyfter\\week_10\\students.csv', 'w', newline = '', encoding='utf-8') as file:
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

    if os.path.exists('C:\\Users\\pc\\Desktop\\Alvaro\\Lyfter\\week_10\\students_control_csv\\students.csv'):
        
        with open('C:\\Users\\pc\\Desktop\\Alvaro\\Lyfter\\week_10\\students_control_csv\\students.csv', 'r', newline = '', encoding='utf-8') as file:
            read = csv.DictReader(file)
            
            # Lista de columnas de notas para convertir
            note_columns = [
                'spanish_note', 'english_note', 'social_note', 'science_note'
            ]
            
            # Leer cada fila y convertir las notas a números flotantes
            for row in read:
                # Para cada columna de nota, intentamos convertir el valor
                for note in note_columns:
                    try:
                        # Convertir las notas a flotantes (si no se puede, asignar 0.0)
                        row[note] = float(row[note]) if row[note] else 0.0
                    except ValueError:
                        # Si la conversión falla (por ejemplo, valor no numérico), asignamos 0.0
                        row[note] = 0.0
                
                # Añadir la fila modificada a la lista
                list_students_data.append(row)
    print('Import completed successfully.')