# Entrada
numeros = input("Ingrese los números separados por espacios: ")
distancia = input("Ingrese la distancia: ")

numeros = numeros.split(" ")
distancia = int(distancia)

# Procesamiento
for x in range(len(numeros)):
	numeros[x] = int(numeros[x])

contador = 0
for i in range(len(numeros)):
	for j in range(i+1, len(numeros)):
		if abs(numeros[i] - numeros[j]) == distancia:
			contador += 1

# Salida
print(contador)