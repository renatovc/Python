# Entrada
lado_hexagono = input()

# Procesamiento
lado_hexagono = int(lado_hexagono)
area_hexagono = ((3 * 3 ** 0.5 * lado_hexagono ** 2) / 2)
area_final = round(area_hexagono, 2)

# Salida
print("El área es", area_final)