# Entrada
numero = input("Ingrese un número para analizar: ")

# Procesamiento
pares_vistos = []
pares_repetidos = []

i = 0
while i < len(numero) - 1:
    par = numero[i] + numero[i + 1]
    
    if par in pares_vistos and par not in pares_repetidos:
        pares_repetidos.append(par)
    elif par not in pares_vistos:
        pares_vistos.append(par)
    
    i += 1

# Salida
if pares_repetidos:
    mayor_par = pares_repetidos[0]
    j = 1
    while j < len(pares_repetidos):
        if int(pares_repetidos[j]) > int(mayor_par):
            mayor_par = pares_repetidos[j]
        j += 1
    print(mayor_par)
else:
    print("No se encontraron coincidencias")