# Entrada
nombre = input("Nombre: ")
tarea_1 = input("Tarea 1: ")
tarea_2 = input("Tarea 2: ")
tarea_3 = input("Tarea 3: ")
controles = input("Controles: ")
guias = input("Guías: ")

# Procesamiento
nombre = nombre.title()

tarea_1 = float(tarea_1)
tarea_2 = float(tarea_2)
tarea_3 = float(tarea_3)
controles = float(controles)
guias = float(guias)

nota_tarea_1 = tarea_1 * 0.1
nota_tarea_2 = tarea_2 * 0.2
nota_tarea_3 = tarea_3 * 0.3
nota_controles = controles * 0.15
nota_guias = guias * 0.25

suma_notas = nota_tarea_1 + nota_tarea_2 + nota_tarea_3 + nota_controles + nota_guias

suma_notas = round(suma_notas, 1)

suma_notas = str(suma_notas)

# Salida
print(nombre + ", tu promedio es " + suma_notas)