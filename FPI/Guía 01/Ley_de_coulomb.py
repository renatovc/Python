# Constante de coulomb: 8.987 * 10**9
# Entrada
carga_1 = input()
carga_2 = input()
distancia = input()

# Procesamiento
carga_1 = carga_1.split("e")
carga_2 = carga_2.split("e")

distancia = float(distancia)

carga_num_1 = float(carga_1[0])
carga_num_01 = float(carga_1[1])

carga_num_2 = float(carga_2[0])
carga_num_02 = float(carga_2[1])

mult_coeficientes = (8.987 * carga_num_1 * carga_num_2)
sum_exponentes = (9 + carga_num_01 + carga_num_02)

fuerza_electroestática = (mult_coeficientes * (10 ** sum_exponentes)) / distancia ** 2

fuerza_electroestática = round(fuerza_electroestática, 2)

# Salida
print(fuerza_electroestática)