## Entrada ##
cant_personajes_preseleccion = int(input())
cant_cupos_torneo = int(input())

participantes = []
i = 0
while i < cant_personajes_preseleccion:
	participante = input()
	participante = participante.split(",")
	participantes.append(participante)
	i += 1

resultado_sorteo = input()
resultado_sorteo = resultado_sorteo.split(",")

## Procesamiento ##
participantes_seleccionados = []

i = 0
while i < len(participantes):
	participant = participantes[i]
	if participant[1] == "MAQUINA DESTRUIDA":
		participantes_seleccionados.append(participant[0])
		participantes.remove(participantes[i])
	i += 1

# Transformo los valores de poder a int
i = 0
while i < len(participantes):
	participantes[i][1] = int(participantes[i][1])
	i += 1

# Ordeno la lista de mayor a menor
i = 0
while i < len(participantes):
	e = 0
	while e < len(participantes) - 1:
		if participantes[e][1] < participantes[e + 1][1]:
			temporal = participantes[e]
			participantes[e] = participantes[e + 1]
			participantes[e + 1] = temporal
		e += 1
	i += 1

i = 0
while i < cant_cupos_torneo:
	participantes_seleccionados.append(participantes[i][0])
	i += 1

if len(participantes_seleccionados) > cant_cupos_torneo:
	participantes_seleccionados.pop(-1)
	if len(participantes_seleccionados) > cant_cupos_torneo:
		participantes_seleccionados.pop(-1)
		if len(participantes_seleccionados) > cant_cupos_torneo:
			participantes_seleccionados.pop(-1)

## Salida ##
print("Y los participantes seleccionados son:")
for u in participantes_seleccionados:
	print(u)

#### PARTE II ####
for i in range(len(resultado_sorteo)):
	resultado_sorteo[i] = int(resultado_sorteo[i])

i = 0
while i < len(resultado_sorteo):
	for i in resultado_sorteo:
		participantes_seleccionados.append(resultado_sorteo[i])
	i += 1

#print(participantes_seleccionados)

######### Tristemente esta tarea no pude completarla, por lo que le falta gran parte del código :( #########