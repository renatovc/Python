texto = input("Ingrese el texto: ")

cant_vocales = 0
for i in texto:
    if i in "aeiouAEIOU":
        cant_vocales += 1

print("El texto tiene", cant_vocales, "vocales")