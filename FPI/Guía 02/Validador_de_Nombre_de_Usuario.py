# Entrada
usuario = input("Usuario: ")

numero_base = 0

# Procesamiento y salida
if len(usuario) >= 6 and len(usuario) <= 32:
  for caracter in usuario:
    if caracter >= str(numero_base) and caracter.isupper():
      print("Válido.")
else:
  print("Inválido.")