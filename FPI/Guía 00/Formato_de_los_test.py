# Entrada
altura = input("Ingrese la altura del cilindro: ")
radio = input("Ingrese el radio de la base del cilindro: ")

altura = float(altura)
radio = float(radio)

# Procesamiento
area_cilindro = round((2 * 3.14 * radio * altura) + (2 * 3.14 * (radio**2)), 2)

# Salida
print("(TEST 30pts)")
print(f"El área del cilindro es: {area_cilindro}")