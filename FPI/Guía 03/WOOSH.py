# Entrada
hechizo = input()
										
# Procesamiento
vocales = []
for i in hechizo:
	if i in "aeiou":
		vocales.append(i)

ascendente = True
descenente = True

for i in range(1, len(vocales)):
	if vocales[i] < vocales[i - 1]:
		ascendente = False
	if vocales[i] > vocales[i - 1]:
		descenente = False

if ascendente:
	print("pulentus")
elif descenente:
	print("bacanus")
else:
	print("cumast")