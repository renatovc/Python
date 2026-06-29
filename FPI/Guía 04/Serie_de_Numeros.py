# Entrada
numeros = input("Ingrese un número entero o ingrese 'FIN' para terminar: ")
numero_sec = []

# Procesamiento
while numeros != "FIN":
	numero_sec.append(numeros)
	numeros = input("Ingrese un número entero o ingrese 'FIN' para terminar: ")

for i in range(len(numero_sec)):
	numero_sec[i] = int(numero_sec[i])

numero_sec.sort()
primer_num = numero_sec[0]
ult_num = numero_sec[-1]
lista_no_primer_ult_num = numero_sec[1 : -1]

complete = True

numeros_inter = list(range(primer_num, ult_num))

for num in range(primer_num + 1, ult_num):
	if num not in lista_no_primer_ult_num:
		complete = False

# Salida
if complete:
	print("Serie completa")
else:
	print("Serie incompleta")