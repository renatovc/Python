# Entrada
genero = input("Ingrese su género: ")
edad = input("Ingrese su edad: ")

genero = len(genero)
edad = int(edad)

# Procesamiento y Salida
if genero == 5 and edad >= 60:
  print("Ud. califica para la tarjeta de tercera edad.")
elif genero == 6 and edad >= 65:
  print("Ud. califica para la tarjeta de tercera edad.")
else:
  print("Ud. no califica para la tarjeta de tercera edad.")