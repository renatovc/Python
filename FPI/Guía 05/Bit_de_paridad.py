# Definiciones
def mensaje_lista(serie):
	return serie.split(" ")

def byt_paridad(byte):
	men = byte[:-1]
	count = 0
	for bit in men:
		if bit == '1':
			count += 1

	if count % 2 == 0:
		return True
	else:
		return False

def ultimo_byte(byte):
	return int(byte[len(byte) - 1])

def correcto(byte):
	if byt_paridad(byte) and ultimo_byte(byte) == 0:
		return True
	if not byt_paridad(byte) and ultimo_byte(byte) == 1:
		return True
	else:
		return False

def es_correcto(serie_byte):
	count = 0
	for byte in serie_byte:
		if correcto(byte):
			count += 1
	return count

def salidas(serie_byte):
	correctos = es_correcto(serie_byte)
	total = len(serie_byte)
	total1 = correctos/total
	if total1 > 0.5:
		print(f">50% mensajes correctos: {correctos} de {total}")
	elif total1 < 0.5:
		print(f"<50% mensajes correctos: {correctos} de {total}")
	else:
		print(f"50% mensajes correctos: {correctos} de {total}")

# Entrada
serie_byte = input("Ingrese la serie de mensajes: ")

# Procesamiento
serie_byte = mensaje_lista(serie_byte)

# Salida
salidas(serie_byte)