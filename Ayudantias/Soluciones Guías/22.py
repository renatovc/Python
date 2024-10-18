# Entrada
q1 = float(input("Ingrese valor de la primera carga: "))
q2 = float(input("Ingrese valor de la segunda carga: "))
distancia = float(input("Ingrese la distancia entre las cargas: "))

# Procesamiento
fuerza = round((q1 * q2) / (distancia ** 2), 10)

# Salida
print("La fuerza es:", str(fuerza))