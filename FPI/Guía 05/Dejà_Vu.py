# Escriba su código acá

#ENTRADA
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input(" Ingrese la cantidad de columnas: "))
datos = input(" Ingrese los datos: ")

matriz = []

#PROCESAMIENTO

numeros = datos.split(",")
fila_11 = numeros[:columnas]
matriz.append(fila_11)

i = columnas
while i <= len(numeros):
	fila_1n = numeros[i:columnas+i]
	matriz.append(fila_1n)
	i += columnas
final = len(matriz)-1
matriz_o = matriz[:final]
 
matriz_original = []
for fila_i in matriz_o:
	fila_i_enteros = []
	for num in fila_i:
		num_entero = int(num)
		fila_i_enteros.append(num_entero)
	matriz_original.append(fila_i_enteros)

#SALIDA 1
print("Matriz Original:")
print(matriz_original)


matriz_v = matriz_o
matriz_v.reverse()

matriz_vertical = []

for fila_j in matriz_v:
	fila_j_enteros = []
	for num in fila_j:
		num_entero = int(num)
		fila_j_enteros.append(num_entero)
	matriz_vertical.append(fila_j_enteros)   

#SALIDA 2
print("Matriz Reflejada Verticalmente:")
print(matriz_vertical)

j = 0
matriz_h = []
while j < len(matriz_o):
	fila_h = matriz_o[j]
	fila_h.reverse()
	matriz_h.append(fila_h)
	j = j+1

matriz_h.reverse()  

matriz_horizontal = []

for fila_k in matriz_h:
	fila_k_enteros = []
	for num in fila_k:
		num_entero = int(num)
		fila_k_enteros.append(num_entero)
	matriz_horizontal.append(fila_k_enteros)  

#SALIDA 3
print("Matriz Reflejada Horizontalmente:")  
print(matriz_horizontal)