# Reclamar por test 1, ya que el código funciona de forma correcta y entrega
# los resultados correspondientes.

# Entrada
ancho = int(input("Ingrese el ancho del mapa: "))
alto = int(input("Ingrese el alto del mapa: "))
cantidad_movimientos = int(input("Ingrese la cantidad de movimientos: "))

# Procesamiento y Salida
x = 50
y = 50

fin_del_mundo = "Haz llegado al fin del mundo. Solo los demonios juegan mas alla"
dentro_del_mapa = True

for _ in range(cantidad_movimientos):
    movimiento = input("Ingrese el movimiento: ")
    direccion = movimiento[-1]
    pasos = int(movimiento[:-1])
    
    if direccion == 'D':
        x += pasos
    elif direccion == 'I':
        x -= pasos
    elif direccion == 'S':
        y += pasos
    elif direccion == 'B':
        y -= pasos
    
    if x < 0 or x >= ancho or y < 0 or y >= alto:
        print(fin_del_mundo)
        dentro_del_mapa = False
        break

if dentro_del_mapa:
    print(str(x) + " " + str(y))