# Entrada
conjunto1 = input("Ingrese los valores 1: ")
conjunto2 = input("Ingrese los valores 2: ")

conjunto1 = conjunto1.split(" ")
conjunto2 = conjunto2.split(" ")

# Procesamiento
conjunto1 = list(conjunto1)
conjunto2 = list(conjunto2)

for i in range(len(conjunto1)):
	conjunto1[i] = int(conjunto1[i])

for i in range(len(conjunto2)):
	conjunto2[i] = int(conjunto2[i])

dif_asimetrica = []
for num in conjunto1:
	if num not in conjunto2:
		dif_asimetrica.append(num)

for num in conjunto2:
	if num not in conjunto1:
		dif_asimetrica.append(num)

dif_asimetrica.sort(reverse=False)

if not dif_asimetrica:
	print("")

# Salida
for i in range(len(dif_asimetrica)):
	if i == len(dif_asimetrica) - 1:
		print(dif_asimetrica[i])
	else:
		print(dif_asimetrica[i], end=" ")