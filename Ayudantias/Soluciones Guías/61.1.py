numero = int(input("Ingrese un número: "))

divisores = [1]
i = 2

while i <= numero // 2:
    if numero % i == 0:
        divisores.append(i)
    i += 1

suma = 0
j = 0
while j < len(divisores):
    suma = suma + divisores[j]
    j += 1

if suma < numero:
    print("Deficiente")
elif suma == numero:
    print("Perfecto")
else:
    print("Abundante")
