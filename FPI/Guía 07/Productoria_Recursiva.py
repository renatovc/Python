def productoria(n):
  if n == 0:
    return 1
  return n * productoria(n - 1)


if __name__ == "__main__":
  # Entrada
  n = int(input("Ingrese un número entero positivo: "))

  # Procesamiento
  res = productoria(n)

  # Salida
  print("La productoria de los", n, "primeros números es:", res)
