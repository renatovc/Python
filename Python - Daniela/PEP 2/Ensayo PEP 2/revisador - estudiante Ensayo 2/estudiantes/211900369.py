# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
#FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO:
# PROFESOR DE TEORÍA:
# PROFESOR DE LABORATORIO:
#
# AUTOR
# NOMBRE: Daniela Belén Castro Añasco
# RUN: 21.190.036-9
# CARRERA: Ingeniería Civil Química

###################

# Función para leer el archivo CSV
def leer_csv(ruta_archivo):
    juegos = []
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = archivo_csv.readlines()
        encabezados = lector_csv[0].strip().split(',')
        for linea in lector_csv[1:]:
            valores = linea.strip().split(',')
            juego = {}
            for i in range(len(encabezados)):
                juego[encabezados[i]] = valores[i]
            juegos.append(juego)
    return juegos

# Función para filtrar los juegos por año
def filtrar_por_año(juegos, año):
    juegos_año = []
    for juego in juegos:
        if juego['Year'] == año:
            juegos_año.append(juego)
    return juegos_año

# Función para calcular las ventas totales
def calcular_ventas_totales(juegos):
    for juego in juegos:
        ventas_totales = (
            float(juego['NA_Sales']) +
            float(juego['EU_Sales']) +
            float(juego['JP_Sales']) +
            float(juego['Other_Sales'])
        )
        juego['Total_Sales'] = ventas_totales
    return juegos

# Función para obtener el top-k ingresados de juegos
def obtener_top_k(juegos, k):
    juegos_ordenados = sorted(juegos, key=ordenar_juegos, reverse=True)
    top_k_juegos = []
    for i in range(min(k, len(juegos_ordenados))):
        top_k_juegos.append(juegos_ordenados[i])
    return top_k_juegos

# Función de clave para ordenar los juegos
def ordenar_juegos(juego):
    return (juego['Total_Sales'], -int(juego['Rank']))

# Función para mostrar los juegos
def mostrar_juegos(juegos):
    for juego in juegos:
        print(f"{juego['Name']}")

# Entrada
ruta_archivo = 'ventas.csv'
año_consulta = input('Ingrese el año a consultar: ')
cant_titulos = int(input('Ingrese la cantidad: '))

# Procesamiento
juegos = leer_csv(ruta_archivo)
juegos_año = filtrar_por_año(juegos, año_consulta)
juegos_año = calcular_ventas_totales(juegos_año)
top_k_juegos = obtener_top_k(juegos_año, cant_titulos)
mostrar_juegos(top_k_juegos)