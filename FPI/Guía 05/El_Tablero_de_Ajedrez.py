# Definiciones
def gen_tablero(piezas):
	tablero = [['  ' for _ in range(8)] for _ in range(8)]

	for entrada in piezas.split(","):
		color = entrada[0]
		pieza = entrada[1]
		columna = ord(entrada[2]) - ord('A')
		fila = - int(entrada[3])

		tablero[fila][columna] = color + pieza

		if 0 <= fila < 8 and 0 <= columna < 8:
			tablero[fila][columna] = color + pieza
			
	return tablero

# Entrada
piezas = input()

# Procesamiento
tablero_final = gen_tablero(piezas)
tab = []

# Salida
for fila in tablero_final:
	tab.append(fila)

print(tab)