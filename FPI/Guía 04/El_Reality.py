# Entrada
participantes = input()
participantes = participantes.split(",")
contador = []
# Procesamiento
i = 0
while i < len(participantes):
	votos = input()
	votos = votos.split(" vota por ")
	contador.append(votos[-1])
	i += 1

maximo = float("-inf")
for nombre in participantes:
	c = 0
	for v in contador:
		if v == nombre:
			c += 1
	if c > maximo:
		maximo = c
		ganador = nombre

# Salida
print(f"Con {maximo} votos, la/el participante {ganador} deja la casa estudio!")