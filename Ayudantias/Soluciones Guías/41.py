# Entrada
nombre1 = input("Ingrese el primer nombre: ")
edad1 = int(input("Ingrese la primera edad: "))
nombre2 = input("Ingrese el segundo nombre: ")
edad2 = int(input("Ingrese la segunda edad: "))
nombre3 = input("Ingrese el tercer nombre: ")
edad3 = int(input("Ingrese la tercera edad: "))
nombre4 = input("Ingrese el cuarto nombre: ")
edad4 = int(input("Ingrese la cuarta edad: "))

# Procesamiento
if edad1 > edad2 and edad1 > edad3 and edad1 > edad4:
    mayor = nombre1
elif edad2 > edad1 and edad2 > edad3 and edad2 > edad4:
    mayor = nombre2
elif edad3 > edad1 and edad3 > edad2 and edad3 > edad4:
    mayor = nombre3
else:
    mayor = nombre4

# Salida
print(mayor)