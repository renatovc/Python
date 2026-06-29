# Definiciones
def obtener_mejor_jugador(datos):
	equipos = {}
	jugadores = datos.split('|')

	for jugador in jugadores:
			info_jugador = jugador.split(',')
			usuario = info_jugador[0]
			equipo = info_jugador[1]
			puntaje = int(info_jugador[2])

			if equipo not in equipos or puntaje > equipos[equipo][1]:
					equipos[equipo] = (usuario, puntaje)

	for equipo, info in equipos.items():
			print(f"{equipo}: {info[0]} con {info[1]} pts")

# Entrada
datos_entrada = input("Ingrese los datos: ")

#Procesamiento
obtener_mejor_jugador(datos_entrada)