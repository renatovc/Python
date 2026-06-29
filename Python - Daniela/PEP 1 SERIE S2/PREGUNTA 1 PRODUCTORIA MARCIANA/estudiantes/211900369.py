# Entrada
sec_digitos = input("Ingrese una secuencia de digitos: ")

# Procesamiento
subsecuencias = []
for i in range(len(sec_digitos)):
    for j in range(i + 1, len(sec_digitos) + 1):
        if sec_digitos[i] == sec_digitos[j - 1]:
            subsecuencias.append(sec_digitos[i:j])

# Calcula el producto de la subsecuencia (lista)
prod = 1
for digito in subsecuencias:
    prod *= int(digito)

# Calcular el producto maximo entre las subsecuencias
max_prod = 0
for sub_sec in subsecuencias:
    prod = 1
    for digito in sub_sec:
        prod *= int(digito)
    if prod > max_prod:
        max_prod = prod

# Salida
print(str(max_prod))