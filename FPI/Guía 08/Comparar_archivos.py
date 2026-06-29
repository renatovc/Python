def comparar(archivo1, archivo2, resultado):
  with open(archivo1, 'r') as f1, open(archivo2, 'r') as f2:
      matriz1 = [list(map(int, linea.split())) for linea in f1.readlines()]
      matriz2 = [list(map(int, linea.split())) for linea in f2.readlines()]

  resultado_matriz = []
  for i in range(len(matriz1)):
      fila_resultado = []
      for j in range(len(matriz1[0])):
          if matriz1[i][j] == matriz2[i][j]:
              fila_resultado.append('O')
          else:
              fila_resultado.append('X')
      resultado_matriz.append(fila_resultado)

  with open(resultado, 'w') as f_resultado:
      for fila in resultado_matriz:
          f_resultado.write(' '.join(map(str, fila)) + '\n')

comparar('Matriz1.txt', 'Matriz2.txt', 'resultado.txt')