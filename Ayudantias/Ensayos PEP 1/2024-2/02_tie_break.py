# Entrada
sec_puntos = input("Ingrese la secuencia de puntos: ")

# Procesamiento
pt_jugador1 = 0
pt_jugador2 = 0
cambio_lado = 6
fin_partido = False

i = 0
while i < len(sec_puntos) and not fin_partido:
    punto = sec_puntos[i]

    if punto == "1":
        pt_jugador1 += 1
    elif punto == "2":
        pt_jugador2 += 1

    print(str(pt_jugador1) + " " + str(pt_jugador2))

    if (pt_jugador1 + pt_jugador2) % cambio_lado == 0:
        print("Cambio de lado")

    if (pt_jugador1 >= 7 or pt_jugador2 >= 7) and abs(pt_jugador1 - pt_jugador2) >= 2:
        fin_partido = True

    i += 1

# Salida
if pt_jugador1 > pt_jugador2:
    print("Jugador 1")
else:
    print("Jugador 2")