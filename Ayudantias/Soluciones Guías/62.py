numero = int(input("Ingrese un número: "))

print(numero)
while numero != 1:
    if numero % 2 == 0:
        numero = numero / 2

    elif numero % 2 == 1:
        numero = (3 * numero) + 1

    print(int(numero))