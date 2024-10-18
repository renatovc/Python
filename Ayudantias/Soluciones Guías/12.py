# Entrada
lado_hexagono = int(input("Ingrese el lado del hexágono: "))

# Procesamiento
area_hexagono = (lado_hexagono ** 2) * ((3 * (3 ** 0.5)) / 2)
area_hexagono = round(area_hexagono, 3)

# Salida
print("El área es", area_hexagono)