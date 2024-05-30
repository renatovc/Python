# Entrada
numero = input()

# Procesamiento y Salida
if '.' in numero:
  print("El número no es entero.")
elif int(numero) % 2 == 0:
  print("par")
else:
  print("impar")