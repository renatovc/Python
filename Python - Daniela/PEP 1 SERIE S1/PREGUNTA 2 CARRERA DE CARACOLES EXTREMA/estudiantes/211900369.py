# Recibir el avance y la distancia
avance = input("Ingrese el avance: ")
distancia = int(input("Ingrese la distancia: "))

# Convertir la entrada a una lista de enteros
avances_str = avance.split(',')
avances = []
for x in avances_str:
    avances.append(int(x))

# Dividir los avances en dos listas, una para cada competidor
mitad = len(avances) // 2
avances_jugador1 = []
avances_jugador2 = []

for i in range(mitad):
    avances_jugador1.append(avances[i])

for i in range(mitad, len(avances)):
    avances_jugador2.append(avances[i])

avances_jugador2.reverse()

# Calcular el avance total de cada jugador
total_jugador1 = 0
total_jugador2 = 0
ganador = "Ambos fallaron"

# Variable para seguir la condición de parada
condicion_de_parada = False

for i in range(mitad):
    if not condicion_de_parada:
        total_jugador1 += avances_jugador1[i]
        total_jugador2 += avances_jugador2[i]

        if total_jugador1 >= distancia and total_jugador2 >= distancia:
            ganador = "Empate"
            condicion_de_parada = True
        elif total_jugador1 >= distancia:
            ganador = "Jugador 1"
            condicion_de_parada = True
        elif total_jugador2 >= distancia:
            ganador = "Jugador 2"
            condicion_de_parada = True

# Imprimimos el resultado
print(ganador)
