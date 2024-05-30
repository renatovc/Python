# Entrada
lista = []
while len(lista) < 10:
    lista.append(input("Ingrese una palabra: "))

# Procesamiento
palabras = []

vocales_min = "aeiou"
vocales_min_acen = "áéíóú"
vocales_max = "AEIOU"
vocales_max_acen = "ÁÉÍÓÚ"

for i in lista:
	if i[0] in vocales_min or i[0] in vocales_min_acen or i[0] in vocales_max or i[0] in vocales_max_acen:
		palabras.append(i)

# Salida
for x in palabras:
	print(x)