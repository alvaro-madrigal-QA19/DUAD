
#****************calcular y mostrar su salario.***************

horas_trabajadas = int(input('Por favor ingrese la cantidad de horas trabajadas: '))
tarifa_por_hora = int(input('Por favor ingrese el monto que usted gana por hora: ₡'))
salario = horas_trabajadas * tarifa_por_hora

print("Su salario es igual a: ₡" + str(salario))




#****************generar email***************

print("*****GENERADOR DE EMAILS EMPRESARIALES*****")
nombre = input('Por favor ingrese su nombre: ').lower()
apellido = input('Por favor ingrese su apellido: ').lower()
nombre_empresa = input('Por favor ingrese el nombre de la empresa donde labora: ').lower()

print(f'Su correo empresarial es el siguiente {(nombre)}.{(apellido)}@{(nombre_empresa)}.com')