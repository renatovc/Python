# Entrada
alcohol_sangre = input("Ingrese los gramos por litro de sangre: ")

alcohol_sangre = float(alcohol_sangre)

# Procesamiento y Salida
if alcohol_sangre >= 4.00:
  print("¿HAY UN MÉDICO EN LA SALA?")
elif alcohol_sangre <= 3.99 and alcohol_sangre >= 3.00:
  print("ESCUCHO BORROSO")
elif alcohol_sangre <= 2.99 and alcohol_sangre >= 1.00:
  print("DANDO JUGO")
elif alcohol_sangre <= 0.99 and alcohol_sangre >= 0.80:
  print("ESTADO DE EBRIEDAD")
elif alcohol_sangre <= 0.79 and alcohol_sangre >= 0.5:
  print("LLAMANDO AL EX")
elif alcohol_sangre <= 0.49 and alcohol_sangre >= 0.3:
  print("BAJO LA INFLUENCIA DEL ALCOHOL")
elif alcohol_sangre <= 0.29 and alcohol_sangre >= 0.2:
  print("AL LÍMITE")
elif alcohol_sangre <= 0.19 and alcohol_sangre >= 0.1:
  print("HAPPY")
elif alcohol_sangre <= 0.09 and alcohol_sangre >= 0.00:
  print("BIEN")
else:
  print("MEDICIÓN ERRONEA")