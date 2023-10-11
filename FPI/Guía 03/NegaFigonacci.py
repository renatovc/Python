# Entrada
numero = int(input())

# Procesamiento
fb_0 = 0
fb_1 = 1

while numero < 0:
	num = fb_0
	fb_0 = fb_1 - fb_0
	fb_1 = num
	numero = numero + 1
	resp = fb_0

# Salida
print(resp)