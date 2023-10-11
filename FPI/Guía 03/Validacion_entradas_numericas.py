# Entrada
numero = ""

# Procesamiento
valido  = False

while not valido:
	valido = True
	numero = input()
	puntos = numero.count(".")
	if numero [0] == "-" or numero[0] == "+":
		i = 1
		while i < len(numero):
			if numero[i] not in "0123456789." or 2 <= puntos:
				print("¡Error de ingreso!")
				valido = False
				i = len(numero)
			i += 1

	else:
		i = 0
		while i < len(numero):
			if numero[i] not in "0123456789." or 2 <= puntos:
				print("¡Error de ingreso!")
				valido = False
				i =len(numero)
			i += 1

	if valido:
		numero = float(numero)
		print(f"Se ha obtenido el número: {numero}")