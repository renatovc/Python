# Entrada
numero = input()
numero = int(numero)

# Procesamiento y Salida
if numero > 0:
	for i in range(numero, 0, -1):
		if numero % i == 0:
			print(i)
else:
	print("Ingrese un número entero positivo.")