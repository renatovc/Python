# Entrada
escenario = input()
escenario = escenario.split("*")

# Procesamiento y Salida
posicion = 0
i = 0
while i < len(escenario):
	if "N" in escenario[i]:
		posicion = i
	i += 1

lugar = escenario[posicion]

abejas = lugar.count("b")

if abejas <= 5:
	print(f"Nic Cage ha sobrevivido al ataque de {abejas} abejas")
else:
	print(f"Nic Cage no lo consiguió, {abejas} abejas pudieron superarlo")
