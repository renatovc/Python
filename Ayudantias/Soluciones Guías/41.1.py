nombres = []
edades = []

# Entrada
nombres.append(input("Ingrese el primer nombre: "))
edades.append(int(input("Ingrese la primera edad: ")))

nombres.append(input("Ingrese el segundo nombre: "))
edades.append(int(input("Ingrese la segunda edad: ")))

nombres.append(input("Ingrese el tercer nombre: "))
edades.append(int(input("Ingrese la tercera edad: ")))

nombres.append(input("Ingrese el cuarto nombre: "))
edades.append(int(input("Ingrese la cuarta edad: ")))

# Procesamiento
mayor_edad = edades[0]
indice_mayor = 0

if edades[1] > mayor_edad:
    mayor_edad = edades[1]
    indice_mayor = 1

if edades[2] > mayor_edad:
    mayor_edad = edades[2]
    indice_mayor = 2

if edades[3] > mayor_edad:
    mayor_edad = edades[3]
    indice_mayor = 3
# Salida
print(nombres[indice_mayor])
