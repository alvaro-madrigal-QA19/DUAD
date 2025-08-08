'''Dada `n` cantidad de notas de un estudiante, calcular:
>> 1. Cuantas notas tiene aprobadas (mayor a 70).
>> 2. Cuantas notas tiene desaprobadas (menor a 70).
>>3. El promedio de todas.
4. El promedio de las aprobadas.
5. El promedio de las desaprobadas.'''



revisar_notas = int(input('Ingrese la cantidad de notas que desea revisar: '))

notas = 0
cantid_aprobadas = 0
cantid_desaprobadas = 0
promedio_total = 0
promedio_aprob = 0
promedio_desaprob = 0

contador = 1

while(contador <= revisar_notas):
    notas = int(input('Ingrese la nota del estudiante: '))

    if(notas >= 70):
        cantid_aprobadas = cantid_aprobadas + 1
        promedio_aprob = (promedio_aprob + notas)
    else:
        cantid_desaprobadas = cantid_desaprobadas + 1
        promedio_desaprob = (promedio_desaprob + notas)


    promedio_total = (promedio_total + notas) 
    contador += 1

promedio_total = promedio_total  / revisar_notas
print(f'Notas Aprobadas: {cantid_aprobadas}')
print(f'Notas Desaprobadas: {cantid_desaprobadas}')
print(f'Promedio Total: {promedio_total}')

if(promedio_aprob > 0):
    promedio_aprob = promedio_aprob  / cantid_aprobadas

if(promedio_desaprob > 0):
    promedio_desaprob = promedio_desaprob  / cantid_desaprobadas
    

print(f'Promedio Aprobado: {promedio_aprob}')
print(f'Promedio Desaprobado: {promedio_desaprob}')
