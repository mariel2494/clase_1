notas_clases = []

salir = 'n'
contador = 0

while salir != 'y':
	contador += 1
	nota = int (input("Ingrese la nota de su clase %d: " % contador))
	notas_clases.append(nota)
	salir = input("¿Desea salir? y/n: ")

total_notas = 0

for nota in notas_clases:
	total_notas += nota

promedio = (total_notas / contador)

print("Su promedio es: %d" % promedio )

if promedio < 60:
	print("Usted esta aplazado")
	if promedio == 1:
		print("excelente")
elif promedio >= 70 and promedio <=80:
	print("Muy bien")
elif promedio >= 90:
	print("Excelente")

 

