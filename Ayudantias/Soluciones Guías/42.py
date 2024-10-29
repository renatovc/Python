# Entrada
contraseña = input("Ingrese su pass: ")

# Procesamiento y salida
if len(contraseña) == 8:
	minuscula = True
	if contraseña == contraseña.upper():
		minuscula = False
		print("Debe tener al menos una minúscula.")

	mayuscula = True
	if contraseña == contraseña.lower():
		mayuscula = False
		print("Debe tener al menos una mayúscula.")

	# Letra
	letra = False
	i = 0
	while not letra and i < 7:
		if contraseña[i].isalpha():
			letra = True
		i = i + 1

	# Dígito
	digito = False
	i = 0
	while not digito and i < 8:
		if contraseña[i].isdigit():
			digito = True
		i = i + 1

	# Coma
	coma = False
	i = 0
	while not coma and i < 8:
		if contraseña[i] == ",":
			coma = True
		i = i + 1

	# Punto y coma
	punto_coma = False
	i = 0
	while not punto_coma and i < 8:
		if contraseña[i] == ";":
			punto_coma = True
		i = i + 1

	if not letra:
		print("Debe tener al menos una letra.")
	if not digito:
		print("Debe tener al menos una dígito.")
	if not coma:
		print("Debe tener al menos una coma.")
	if not punto_coma:
		print("Debe tener al menos una punto y coma.")

	if mayuscula and minuscula and letra and digito and coma and punto_coma:
		print("Su password cumple con todas las reglas.")
else:
	print("Debe tener 8 caracteres.")