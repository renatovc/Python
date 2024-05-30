# Entrada
prom_actividades_clases = input(
 "Ingrese el promedio de actividades en clases: ")
prom_guias = input("Ingrese el promedio de guías: ")
nota_tarea_1 = input("Ingrese la nota de la tarea 1: ")
nota_tarea_2 = input("Ingrese la nota de la tarea 2: ")
nota_tarea_3 = input("Ingrese la nota de la tarea 3: ")
falta_codigo_honor = input("Tienes falta al código de honor (YES/NO): ")

prom_actividades_clases = float(prom_actividades_clases)
prom_guias = float(prom_guias)
nota_tarea_1 = float(nota_tarea_1)
nota_tarea_2 = float(nota_tarea_2)
nota_tarea_3 = float(nota_tarea_3)
falta_codigo_honor = falta_codigo_honor.upper()

# Procesamiento
promedio = ((prom_actividades_clases * 15) / 100) + (
 (prom_guias * 25) / 100) + ((nota_tarea_1 * 10) / 100) + (
  (nota_tarea_2 * 20) / 100) + ((nota_tarea_3 * 30) / 100)

promedio_examen = (3.96 - ((promedio * 60) / 100)) / 0.4

if falta_codigo_honor == "NO":
	if promedio >= 3.95:
		print(f"Aprobado/a {round(promedio, 1)}")
	elif promedio <= 2.94:
		print(f"Reprobado/a {round(promedio, 1)}")
	elif promedio >= 2.95:
		print(f"Debe rendir examen y necesita al menos un {round(promedio_examen, 1)}")
elif falta_codigo_honor == "YES" and promedio >= 4.00:
	print(f"Aprobado/a {round(promedio, 1)}")
elif falta_codigo_honor == "YES" and promedio <= 3.99:
	print(f"Reprobado/a {round(promedio, 1)}")