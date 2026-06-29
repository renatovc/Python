# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
#FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO:
# PROFESOR DE TEORÍA:
# PROFESOR DE LABORATORIO:
#
# AUTOR
# NOMBRE: DANIELA BELEN CASTRO AÑAZCO
# RUN: 21.190.036-9
# CARRERA: INGENIERIA CIVIL QUÍMICA

###################

#
def leer_csv(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

        print(lineas)

# Entrada
ruta_archivo = 'Resultados.csv'

leer_csv(ruta_archivo)