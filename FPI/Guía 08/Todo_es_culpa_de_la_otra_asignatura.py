import csv

def comparar(universidad, asignatura1, asignatura2):
  with open("Alumnos.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=";")

    columnas = next(csv_reader)

    indice_universidad = columnas.index("Universidad")
    indice_asignatura1 = columnas.index(asignatura1)
    indice_asignatura2 = columnas.index(asignatura2)

    contador = 0

    for row in csv_reader:
      if row[indice_universidad] == universidad:
        nota_asignatura1 = float(row[indice_asignatura1])
        nota_asignatura2 = float(row[indice_asignatura2])

        if nota_asignatura1 < 4.0 and nota_asignatura2 < 4.0:
          contador += 1

  return contador