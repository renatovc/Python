numero = int(input("Ingrese un número: "))

divisores = [1]  # Start with 1, since it's always a divisor

for i in range(2, (numero // 2) + 1):
    if numero % i == 0:
        divisores.append(i)

suma = 0
for i in divisores:
    suma = suma + i

if suma < numero:
    print("Deficiente")
elif suma == numero:
    print("Perfecto")
else:
    print("Abundante")
