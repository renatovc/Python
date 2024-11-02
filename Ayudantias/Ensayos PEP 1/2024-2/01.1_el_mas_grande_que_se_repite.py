numero = input("Ingrese un número para analizar: ")

subcadenas = []

i = 0
while i < len(numero) - 1:
    j = i + 2
    while j <= len(numero):
        subcadena = numero[i:j]
        subcadenas.append(subcadena)
        j += 1
    i += 1

subcadenas_validas = []

i = 0
while i < len(subcadenas):
    j = i + 1
    encontrado = False
    while j < len(subcadenas) and not encontrado:
        if subcadenas[i] == subcadenas[j]:
            subcadenas_validas.append(int(subcadenas[i]))
            encontrado = True
        j += 1
    i += 1

if len(subcadenas_validas) > 0:
    maximo = subcadenas_validas[0]
    i = 1
    while i < len(subcadenas_validas):
        if subcadenas_validas[i] > maximo:
            maximo = subcadenas_validas[i]
        i += 1
    print(maximo)
else:
    print("No se encontraron coincidencias")