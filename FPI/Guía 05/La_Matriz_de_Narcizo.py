valores_1 = []
valores_2 = []
valores_3 = []

# Entrada
while len(valores_1) < 3:
	valores_1.append(int(input("Ingrese un número: ")))

while len(valores_2) < 3:
	valores_2.append(int(input("Ingrese un número: ")))

while len(valores_3) < 3:
	valores_3.append(int(input("Ingrese un número: ")))


# Procesamiento y Salida
print(f"Matriz Original:\n[{valores_1}, {valores_2}, {valores_3}]")

valores_1_inv = valores_1.copy()
valores_2_inv = valores_2.copy()
valores_3_inv = valores_3.copy()

print(
 f"Matriz Reflejada Verticalmente:\n[{valores_3_inv}, {valores_2_inv}, {valores_1_inv}]"
)

print(
 f"Matriz Reflejada Horizontalmente:\n[{valores_1_inv[-1::-1]}, {valores_2_inv[-1::-1]}, {valores_3_inv[-1::-1]}]"
)