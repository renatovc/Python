cant_rondas = int(input("Ingrese la cantidad de rondas: "))

jugadas_j1 = []
jugadas_j2 = []

i = 0
while i < cant_rondas:
    jugador_1 = input("Ingrese la jugada del primer jugador: ")
    jugadas_j1.append(jugador_1)
    i += 1

j = 0
while j < cant_rondas:
    jugador_2 = input("Ingrese la jugada del segundo jugador: ")
    jugadas_j2.append(jugador_2)
    j += 1

n_ganadas_j1 = 0
n_ganadas_j2 = 0

for k in range(cant_rondas):
    j1 = jugadas_j1[k]
    j2 = jugadas_j2[k]

    if (j1 == "piedra" and j2 == "tijera") or (j1 == "tijera" and j2 == "papel") or (j1 == "papel" and j2 == "piedra"):
        n_ganadas_j1 += 1
    elif (j2 == "piedra" and j1 == "tijera") or (j2 == "tijera" and j1 == "papel") or (j2 == "papel" and j1 == "piedra"):
        n_ganadas_j2 += 1

if n_ganadas_j1 > n_ganadas_j2:
    print("Gana jugador 1")
elif n_ganadas_j2 > n_ganadas_j1:
    print("Gana jugador 2")
else:
    print("Empate")