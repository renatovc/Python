# Entrada
notas = input()
notas = notas.split(";")
notas = [int(nota) for nota in notas]

# Procesamiento
total = 1
for number in notas:
	total *= number

enesima = 1 / len(notas)
media = round(total ** enesima, 2)

# Salida
print(f"La media geometrica es {media}.")