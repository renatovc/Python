# Entradas
matriz_1 = print("Matriz 1:")
matriz_1_a = input()
matriz_1_b = input()
matriz_1_c = input()
matriz_1_d = input()

matriz_2 = print("Matriz 2:")
matriz_2_a = input()
matriz_2_b = input()
matriz_2_c = input()
matriz_2_d = input()

# Procesamiento
matriz_1_a = float(matriz_1_a)
matriz_1_b = float(matriz_1_b)
matriz_1_c = float(matriz_1_c)
matriz_1_d = float(matriz_1_d)

matriz_2_a = float(matriz_2_a)
matriz_2_b = float(matriz_2_b)
matriz_2_c = float(matriz_2_c)
matriz_2_d = float(matriz_2_d)

# Suma de matrices
matriz_suma_a = round(matriz_1_a + matriz_2_a, 2)
matriz_suma_b = round(matriz_1_b + matriz_2_b, 2)
matriz_suma_c = round(matriz_1_c + matriz_2_c, 2)
matriz_suma_d = round(matriz_1_d + matriz_2_d, 2)

matriz_suma_a = str(matriz_suma_a)
matriz_suma_b = str(matriz_suma_b)
matriz_suma_c = str(matriz_suma_c)
matriz_suma_d = str(matriz_suma_d)

# Multiplicación de matrices
matriz_mult_a = round((matriz_1_a * matriz_2_a) + (matriz_1_b * matriz_2_c), 2)
matriz_mult_b = round((matriz_1_a * matriz_2_b) + (matriz_1_b * matriz_2_d), 2)
matriz_mult_c = round((matriz_1_c * matriz_2_a) + (matriz_1_d * matriz_2_c), 2)
matriz_mult_d = round((matriz_1_c * matriz_2_b) + (matriz_1_d * matriz_2_d), 2)

matriz_mult_a = str(matriz_mult_a)
matriz_mult_b = str(matriz_mult_b)
matriz_mult_c = str(matriz_mult_c)
matriz_mult_d = str(matriz_mult_d)

# Determinante matrices
determinante_matriz_1 = (matriz_1_a * matriz_1_d) - (matriz_1_c * matriz_1_b)
determinante_matriz_2 = (matriz_2_a * matriz_2_d) - (matriz_2_c * matriz_2_b)

determinante_matriz_1 = round(determinante_matriz_1, 2)
determinante_matriz_2 = round(determinante_matriz_2, 2)

# Salida
print(
  f"La suma de las matrices es\n{matriz_suma_a} {matriz_suma_b}\n{matriz_suma_c} {matriz_suma_d}\nLa multiplicación de las matrices es\n{matriz_mult_a} {matriz_mult_b}\n{matriz_mult_c} {matriz_mult_d}\nLos determinantes de las matrices son {determinante_matriz_1} y {determinante_matriz_2}"
)