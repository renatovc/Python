# Entradas
producto_1 = input()
precio_producto_1 = input()
cantidad_producto_1 = input()

producto_2 = input()
precio_producto_2 = input()
cantidad_producto_2 = input()

# Procesamiento
precio_producto_1 = float(precio_producto_1)
cantidad_producto_1 = float(cantidad_producto_1)

precio_producto_2 = float(precio_producto_2)
cantidad_producto_2 = float(cantidad_producto_2)

total_producto_1 = precio_producto_1 * cantidad_producto_1
total_producto_2 = precio_producto_2 * cantidad_producto_2

total_productos = total_producto_1 + total_producto_2
 
iva_producto_1 = ((precio_producto_1 * 19) * cantidad_producto_1) / 119
iva_producto_2 = ((precio_producto_2 * 19) * cantidad_producto_2) / 119

iva_total = iva_producto_1 + iva_producto_2


total_producto_1 = str(round(total_producto_1, 2))
total_producto_2 = str(round(total_producto_2, 2))
total_productos = str(round(total_productos, 2))
iva_total = str(round(iva_total, 2))

# Salida
print("El total para " + producto_1 + " es " + total_producto_1 + ".\n"
      "El total para " + producto_2 + " es " + total_producto_2 + ".\n"
      "El valor total de la compra es " + total_productos + ", con " +
      iva_total + " en impuestos.")