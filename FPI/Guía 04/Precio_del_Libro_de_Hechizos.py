# CONST
PRECIO_POR_RANGO = [5, 10, 40, 90, 160, 250, 360, 490, 640, 810]
PRECIO_BASE = 15

# Entrada
hechizos = input()
hechizos = hechizos.split(",")
hechizos = [int(hechizo) for hechizo in hechizos]

# Procesamiento
i = 0
total = 0
while i < len(hechizos):
	total += hechizos[i] * PRECIO_POR_RANGO[i]
	i += 1

valor = total + PRECIO_BASE

# Salida
print(f"El libro tiene un costo de {valor} po.")