def cargar_laberinto(nombre):
  laberinto = []
  if nombre.endswith(".lab"):
    with open(nombre, "r") as f:
      for line in f:
        row = line.strip().split()
        laberinto.append(row)

  else:
    return []

  return laberinto


def encontrar_entrada(laberinto):
  for i in range(len(laberinto)):
    row = laberinto[i]
    for j in range(len(row)):
      cell = row[j]
      if cell == "EE":
        return [i, j]


def encontrar_salida(laberinto):
  for i in range(len(laberinto)):
    row = laberinto[i]
    for j in range(len(row)):
      cell = row[j]
      if cell == "SS":
        return [i, j]


def encontrar_portal(laberinto, x, y):
  for i in range(len(laberinto)):
    for j in range(len(laberinto)):
      if laberinto[i][j] == "PP" and (i != x or j != y):
        return [i, j]


'''
def recuperar_camino(laberinto):
  entrada = encontrar_entrada(laberinto)
  salida = encontrar_salida(laberinto)
  x, y = entrada
  salida_x, salida_y = salida
  camino = ["Entrada"]

  while [x, y] != [salida_x, salida_y]:
    casilla_ac = laberinto[x][y]

    if casilla_ac == "**":
      # Suponiendo el camino siempre libre
      camino.append("DE")
      y += 1
    elif casilla_ac == "EE":
      camino.append("Entrada")
    elif casilla_ac == "SS":
      camino.append("Salida")
    elif casilla_ac == "PP":
      portal_one = encontrar_portal(laberinto, x, y)
      x, y = portal_one
      camino.append("Portal")

  camino.append("Salida")
  return camino
'''