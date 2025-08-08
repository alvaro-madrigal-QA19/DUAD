cantidad_notas = int(input("Ingrese la cantidad de notas: "))
notas_agregadas = []

for n in range(1,cantidad_notas + 1):
    nota = int(input("Nota: "))
    notas_agregadas.append(nota)

mayor_igual_70 = 0
menor_70 = 0

notas_aprobadas = []
notas_desaprobadas = []

for nota in notas_agregadas:
    if nota >=70:
        mayor_igual_70 += 1
        notas_aprobadas.append(nota)
    else:
        menor_70 += 1
        notas_desaprobadas.append(nota)

promedio_total = sum(notas_agregadas) / len(notas_agregadas)

if notas_aprobadas:
    promedio_aprobadas = sum(notas_aprobadas) / len(notas_aprobadas)

else:
    promedio_aprobadas = 0

if notas_desaprobadas:
    promedio_desaprobadas = sum(notas_desaprobadas) / len(notas_desaprobadas)

else:
    promedio_desaprobadas = 0


print("Cantidad de notas aprobadas", mayor_igual_70)
print("Cantidad de notas desaprobadas", menor_70)
print("El promedio de todas las notas: ", promedio_total)
print("Promedio de notas aprobadas:", promedio_aprobadas)
print("Promedio de notas desaprobadas:", promedio_desaprobadas)