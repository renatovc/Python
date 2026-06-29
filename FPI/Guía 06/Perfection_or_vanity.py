# Bloque Definiciones
def obtener_divisores(n):
  dividers = [1]

  for i in range(2, (n // 2) + 1):
    if n % i == 0:
      dividers.append(i)

  dividers.append(n)

  return dividers


def es_perfecto(n):
  dividers = obtener_divisores(n)
  sum_div = sum(dividers)

  return sum_div == 2 * n