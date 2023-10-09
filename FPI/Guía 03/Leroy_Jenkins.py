# Entrada
entrada = ""
frases = []

# Procesamiento y Salida
ATAQUE = "LEEEEEEEEEROY JENKINS!"

while entrada != ATAQUE:
	entrada = input()
	frases.append(entrada)
	
	if entrada == ATAQUE:
		poder = 2 ** (len(frases) - 1)
		print(f"AL ATAQUE!!!, CON PODER DE: {poder}")