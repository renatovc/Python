# Entrada
secuencia = input("Ingrese la secuencia de puntos: ")

# Procesamiento
puntos_jugador_1 = 0
puntos_jugador_2 = 0
fin_partido = False

for punto in secuencia:
    if not fin_partido:
        if punto == "1":
            puntos_jugador_1 += 1
        elif punto == "2":
            puntos_jugador_2 += 1

        print(puntos_jugador_1, puntos_jugador_2)

        if (puntos_jugador_1 + puntos_jugador_2) % 6 == 0:
            print("Cambio de lado")

        if (puntos_jugador_1 >= 7 or puntos_jugador_2 >= 7) and abs(puntos_jugador_1 - puntos_jugador_2) >= 2:
            fin_partido = True

# Salida
if puntos_jugador_1 > puntos_jugador_2:
    print("El ganador es Jugador 1")
else:
    print("El ganador es Jugador 2")
