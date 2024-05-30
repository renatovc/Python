# Entrada
cant_competidores = input()
cant_competidores = int(cant_competidores)

# Procesamiento
snatch = []
dos_pasos = []

i = 0
while i < cant_competidores:
	snatch_1 = int(input())
	snatch_2 = int(input())
	snatch_3 = int(input())
	dos_pasos_1 = int(input())
	dos_pasos_2 = int(input())
	dos_pasos_3 = int(input())

	snatch.append([snatch_1, snatch_2, snatch_3])
	dos_pasos.append([dos_pasos_1, dos_pasos_2, dos_pasos_3])

	i += 1

maximo = max(snatch[0]) + max(dos_pasos[0])
posicion_maxima = 0
i = 1

while i < len(snatch):
	if maximo < (max(snatch[i]) + max(dos_pasos[i])):
		maximo = max(snatch[i]) + max(dos_pasos[i])
		posicion_maxima = i
	i += 1
# Salida
print(f"El competidor {posicion_maxima + 1} ha ganado con {maximo} kg.")