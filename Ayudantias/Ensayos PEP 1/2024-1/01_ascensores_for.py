# Entrada
posicion_inicial_ascensor_izq = int(input("Ingrese piso ascensor izquierdo: "))
posicion_inicial_ascensor_der = int(input("Ingrese piso ascensor derecho: "))
llamados_ascensor = input("Ingrese llamados de ascensor: ") # 45678

pisos_solicitados = []

# Procesamiento y salidas
for i in llamados_ascensor:
    pisos_solicitados.append(int(i))

for i in range(len(pisos_solicitados)):
    posicion_actual_ascensor_izq = abs(posicion_inicial_ascensor_izq - pisos_solicitados[i])
    posicion_actual_ascensor_der = abs(posicion_inicial_ascensor_der - pisos_solicitados[i])

    if posicion_actual_ascensor_izq == posicion_actual_ascensor_der:
        print("Izquierdo")
        posicion_inicial_ascensor_izq = pisos_solicitados[i]
    else:
        if posicion_actual_ascensor_izq < posicion_actual_ascensor_der:
            posicion_inicial_ascensor_izq = pisos_solicitados[i]
            print("Izquierdo")
        elif posicion_actual_ascensor_der < posicion_actual_ascensor_izq:
            posicion_inicial_ascensor_der = pisos_solicitados[i]
            print("Derecho")