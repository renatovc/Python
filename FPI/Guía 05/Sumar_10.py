# Entrada
numero = input("Ingrese un número entero positivo: ")

# Procesamiento
print(numero)

numero_list = list(numero)

i = 0
x = 1
while i < len(numero_list) and x < len(numero_list):
	numero_list[i] = int(numero_list[i])
	numero_list[x] = int(numero_list[x])
	sum = numero_list[i] + numero_list[x]
	if sum == 10:
		numero_list.pop(i)
		numero_list.pop(x-1)
		i -= 2
		x -= 2

		n = 0
		while n < len(numero_list):
			numero_list[n] = str(numero_list[n])
			n += 1
		numero_act = "".join(numero_list)
		print(numero_act)
	i += 1
	x += 1