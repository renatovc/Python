def leer_matriz(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        matriz = [list(map(int, linea.split())) for linea in lineas]
    return matriz

def comparar_matrices(matriz1, matriz2):
    coincidencias = sum(matriz1[i][j] == matriz2[i][j] for i in range(len(matriz1)) for j in range(len(matriz1[0])))
    return coincidencias

def main():
    num_archivos = 10
    archivos = ["Matriz{}.txt".format(i) for i in range(1, num_archivos + 1)]

    with open("resultado.txt", 'w') as resultado:
        for i in range(num_archivos):
            matriz_actual = leer_matriz(archivos[i])
            resultado.write("Matriz {}\n".format(i + 1))
            
            for j in range(num_archivos):
                if i != j:
                    matriz_comparar = leer_matriz(archivos[j])
                    coincidencias = comparar_matrices(matriz_actual, matriz_comparar)
                    resultado.write("   Matriz {}: {} elementos coinciden.\n".format(j + 1, coincidencias))

if __name__ == "__main__":
    main()
