# Entrada
operacion = input("Operación:\n")

# Procesamiento y salida
operador = operacion[0]
valores = operacion[1:]

numeros = valores.split(" ")

primer_valor = int(numeros[0])
segundo_valor = int(numeros[1])

if operador == "+":
	print(primer_valor + segundo_valor)
elif operador == "-":
	print(primer_valor - segundo_valor)
elif operador == "*":
	print(primer_valor * segundo_valor)
elif operador == "/":
	print(primer_valor // segundo_valor)
else:
	print("Operación inválida")