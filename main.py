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

print("Su promedio es: %d" % (total_notas / contador))