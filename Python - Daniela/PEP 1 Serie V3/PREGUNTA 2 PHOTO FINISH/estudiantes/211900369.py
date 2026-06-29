# Verificar test case 1-2-10
# Entrada
primer_avance = input("Ingrese el primer avance: ")
segundo_avance = input("Ingrese el segundo avance: ")
distancia_objetivo = int(input("Ingrese la distancia: "))

# Procesamiento
primer_avance = primer_avance.split('-')
segundo_avance = segundo_avance.split('-')

distancia_jugador_1 = 0
distancia_jugador_2 = 0

fotograma_jugador_1 = len(primer_avance) + 1  # inicializamos con un valor más alto
fotograma_jugador_2 = len(segundo_avance) + 1  # inicializamos con un valor más alto

i = 0
encontro_jugador_1 = False
encontro_jugador_2 = False

while i < len(primer_avance) or i < len(segundo_avance):
    if i < len(primer_avance) and not encontro_jugador_1:
        distancia_jugador_1 += int(primer_avance[i])
        if distancia_jugador_1 >= distancia_objetivo:
            fotograma_jugador_1 = i + 1
            encontro_jugador_1 = True
    
    if i < len(segundo_avance) and not encontro_jugador_2:
        distancia_jugador_2 += int(segundo_avance[i])
        if distancia_jugador_2 >= distancia_objetivo:
            fotograma_jugador_2 = i + 1
            encontro_jugador_2 = True
    
    i += 1

# Salida
if distancia_jugador_1 < distancia_objetivo and distancia_jugador_2 < distancia_objetivo:
    print("Ambos fallaron")
elif fotograma_jugador_1 < fotograma_jugador_2:
    print("Jugador 1")
elif fotograma_jugador_2 < fotograma_jugador_1:
    print("Jugador 2")
else:
    print("Empate")
