# Entrada
nombre = input("Nombre: ")
act_clases = float(input("Actividades en clases: "))
ensayo_pep = float(input("Ensayos de prueba: "))
p1 = float(input("Prueba 1: "))
p2 = float(input("Prueba 2: "))

# Procesamiento
promedio = round((act_clases * 0.15) + (ensayo_pep * 0.05) + (p1 * 0.4) + (p2 * 0.4), 1)

# Salida
print(nombre + ", tu promedio es " + str(promedio))