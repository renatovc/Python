# Entrada
la_ola = input()

# Procesamiento y Salida
for i in range(len(la_ola)):
	olita = la_ola[:i] + la_ola[i].upper() + la_ola[i+1:]
	print(olita)