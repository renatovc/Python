numeros = []
bases = []

# Entrada
numero = input()
numero = numero.split(" ")

# Procesamiento
for i in range(len(numero)):
	if "," in numero[i]:
		numero[i] = numero[i].split(",")
		numeros.append(numero[i][0])
		bases.append(numero[i][1])

i = 0
while i < len(bases):
	bases[i] = int(bases[i])
	i += 1

# Salida
i = 0
while i < len(numeros) and i < len(bases):
	print(str(numeros[i]) + " " + str(bases[i]) + " = " + str(int(numeros[i], bases[i])))
	i += 1