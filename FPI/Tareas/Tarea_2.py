### Definiciones auxiliares
def posicion_en_tablero(pos):
  columna = pos[0]
  fila = int(pos[1])

  return columna, fila


## Definición 1: validar la posición
def validar_posicion(pos, tablero):
  columnas_val = "ABCDEFGH"
  columna, fila = posicion_en_tablero(pos)

  if columna not in columnas_val or fila < 1 or fila > 8:
    return -1

  fila_in = 8 - fila
  columna_in = columnas_val.index(columna)

  if tablero[fila_in][columna_in] != "  ":
    return 1

  return 0


## Definición 2: imprimir tablero
def entregar_tablero(piezas):
  tablero = []
  for _ in range(8):
    fila = []
    for _ in range(8):
      fila.append("  ")
    tablero.append(fila)

  elementos = piezas.split(",")

  for elemento in elementos:
    if len(elemento) == 4:
      color = elemento[0]
      pieza = elemento[1]
      columna = elemento[2]
      fila = elemento[3]

      if color in ("B", "N") and pieza in ('P', 'T', 'C', 'A', 'D','R') and columna in ('A', 'B', 'C', 'D', 'E', 'F', 'G','H') and fila in ('1', '2', '3', '4', '5', '6','7', '8'):
        fila_ind = 8 - int(fila)
        columna_ind = ord(columna) - ord("A")
        pieza_y_color = color + pieza

        if tablero[fila_ind][columna_ind] == "  ":
          tablero[fila_ind][columna_ind] = pieza_y_color

  return tablero


## Definición 3: validación de juego
def es_valido(tablero):
  cont_blancas_p = 0
  cont_blancas_t = 0
  cont_blancas_c = 0
  cont_blancas_a = 0
  cont_blancas_d = 0
  cont_blancas_r = 0

  cont_negras_p = 0
  cont_negras_t = 0
  cont_negras_c = 0
  cont_negras_a = 0
  cont_negras_d = 0
  cont_negras_r = 0

  rey_blanco_pres = False
  rey_negro_pres = False

  alfil_blanco_negra = False
  alfil_blanco_blanco = False
  alfil_negro_negro = False
  alfil_negro_blanco = False

  peones_blancos_filas_correctas = True
  peones_negros_filas_correctas = True

  for fila_ind in range(8):
    for columna_ind in range(8):
      pieza = tablero[fila_ind][columna_ind]

      if pieza != "  ":
        jugador = pieza[0]
        tipo_pieza = pieza[1]

        if jugador == "B":
          if tipo_pieza == "P":
            cont_blancas_p += 1
          elif tipo_pieza == "T":
            cont_blancas_t += 1
          elif tipo_pieza == "C":
            cont_blancas_c += 1
          elif tipo_pieza == "A":
            cont_blancas_a += 1
          elif tipo_pieza == "D":
            cont_blancas_d += 1
          elif tipo_pieza == "R":
            cont_blancas_r += 1

          if tipo_pieza == "R":
            rey_blanco_pres = True

          if jugador == "B" and tipo_pieza == "A":
            if (fila_ind + columna_ind) % 2 == 0:
              alfil_blanco_blanco = True
            elif (fila_ind + columna_ind) % 2 == 1:
              alfil_blanco_negra = True

          if tipo_pieza == "P" and (fila_ind == 0 or fila_ind == 7):
            peones_blancos_filas_correctas = False

        # Reviso las piezas Negras en tablero
        else:
          if tipo_pieza == "P":
            cont_negras_p += 1
          elif tipo_pieza == "T":
            cont_negras_t += 1
          elif tipo_pieza == "C":
            cont_negras_c += 1
          elif tipo_pieza == "A":
            cont_negras_a += 1
          elif tipo_pieza == "D":
            cont_negras_d += 1
          elif tipo_pieza == "R":
            cont_negras_r += 1

          if tipo_pieza == "R":
            rey_negro_pres = True

          if jugador == "N" and tipo_pieza == "A":
            if (fila_ind + columna_ind) % 2 == 0:
              alfil_negro_negro = True
            elif (fila_ind + columna_ind) % 2 == 1:
              alfil_negro_blanco = True

          if tipo_pieza == "P" and (fila_ind == 0 or fila_ind == 7):
            peones_negros_filas_correctas = False

  # Verifico que las variables contandores esten dentro de los rangos de piezas correspondiente
  condiciones_piezas = (cont_blancas_p <= 8 and cont_negras_p <= 8
                        and cont_blancas_t <= 2 and cont_negras_t <= 2
                        and cont_blancas_d <= 1 and cont_negras_d <= 1
                        and cont_blancas_c <= 2 and cont_negras_c <= 2
                        and cont_blancas_a <= 2 and cont_negras_a <= 2
                        and cont_blancas_r == 1 and cont_negras_r == 1)

  condiciones_alfiles_fila = (alfil_blanco_blanco and alfil_blanco_negra and alfil_negro_negro and alfil_negro_blanco)

  condiciones_peones_fila = peones_blancos_filas_correctas and peones_negros_filas_correctas

  # Retorno todas las verificaciones para que de True o False
  return condiciones_piezas and condiciones_peones_fila and condiciones_alfiles_fila


## Definición 4: validar si hay jaque
def hay_jaque(tablero):
  rey_blanco = encontrar_posicion("BR", tablero)
  rey_negro = encontrar_posicion("NR", tablero)

  jaque_blanco = rey_en_jaque(rey_blanco, tablero, tablero)
  jaque_negro = rey_en_jaque(rey_negro, tablero, tablero)

  if jaque_blanco and jaque_negro:
    return 2
  elif jaque_blanco:
    return 0
  elif jaque_negro:
    return 1
  else:
    return -1


### Definiciones auxiliares para "Definición 4"
# Definición auxiliar para encontrar la posición
def encontrar_posicion(pieza, tablero):
  for fila_ind in range(8):
    for columna_ind in range(8):
      if tablero[fila_ind][columna_ind] == pieza:
        return (fila_ind, columna_ind)

  return None


# Definición para determinar si el rey está en jaque
def rey_en_jaque(posicion_rey, oponente, tablero):
  for fila_ind in range(8):
    for columna_ind in range(8):
      pieza = tablero[fila_ind][columna_ind]
      if pieza[0] == oponente and es_movimiento_valido(pieza, (fila_ind, columna_ind), posicion_rey):
        return True

  return False


# Definición para determinar si el movimiento es válido
def es_movimiento_valido(pieza, origen, destino):
  tipo_pieza = pieza[1]
  if tipo_pieza == "P":
    return es_movimiento_peon(pieza[0], origen, destino)
  elif tipo_pieza == "T":
    return es_movimiento_torre(origen, destino)
  elif tipo_pieza == "C":
    return es_movimiento_caballo(origen, destino)
  elif tipo_pieza == "A":
    return es_movimiento_alfil(origen, destino)
  elif tipo_pieza == "D":
    return es_movimiento_dama(origen, destino)
  elif tipo_pieza == "R":
    return es_movimiento_rey(origen, destino)


### Definciónes auxiliares para def es_movimiento_valido
# Definición para validar movimiento del peon
def es_movimiento_peon(color, origen, destino):
  fila_origen, columna_origen = origen
  fila_destino, columna_destino = destino

  if color == "B":
    return fila_destino == fila_origen - 1 and abs(columna_destino - columna_destino) == 1
  else:
    return fila_destino == fila_origen + 1 and abs(columna_destino - columna_origen) == 1


# Definición para el movimiento de la torre
def es_movimiento_torre(origen, destino):
  fila_origen, columna_origen = origen
  fila_destino, columna_destino = destino

  return fila_origen == fila_destino or columna_origen == columna_destino


# Definición para el movimiento del caballo
def es_movimiento_caballo(origen, destino):
  fila_origen, columna_origen = origen
  fila_destino, columna_destino = destino

  return (abs(fila_destino - fila_origen) == 2 and abs(columna_destino - columna_origen) == 1) or (abs(columna_destino - columna_origen) == 2 and abs(fila_destino - fila_origen) == 1)


# Definición para el movimiento del alfil
def es_movimiento_alfil(origen, destino):
  fila_origen, columna_origen = origen
  fila_destino, columna_destino = destino

  return abs(fila_destino - fila_origen) == abs(columna_destino - columna_origen)


# Definición para el movimiento de la reina
def es_movimiento_dama(origen, destino):
  return es_movimiento_torre(origen, destino) or es_movimiento_alfil(origen, destino)


# Definición para el movimiento del rey
def es_movimiento_rey(origen, destino):
  fila_origen, columna_origen = origen
  fila_destino, columna_destino = destino

  return abs(fila_destino - fila_origen) <= 1 and abs(columna_destino - columna_origen) <= 1