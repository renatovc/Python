valor1 = int(input("Ingrese un valor: "))
valor2 = int(input("Ingrese un valor: "))
valor3 = int(input("Ingrese un valor: "))
valor4 = int(input("Ingrese un valor: "))
valor5 = int(input("Ingrese un valor: "))
valor6 = int(input("Ingrese un valor: "))
valor7 = int(input("Ingrese un valor: "))
valor8 = int(input("Ingrese un valor: "))
valor9 = int(input("Ingrese un valor: "))
valor10 = int(input("Ingrese un valor: "))
divisor = int(input("Ingrese número a evaluar: "))

lista_elementos = [valor1, valor2, valor3, valor4, valor5, valor6, valor7, valor8, valor9, valor10]

lista_divisores = []

i = 0
while i < len(lista_elementos):
    if lista_elementos[i] % divisor == 0:
        lista_divisores.append(lista_elementos[i])
    i += 1

print(lista_elementos)
print(len(lista_divisores))