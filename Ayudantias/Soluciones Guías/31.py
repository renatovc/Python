# Entrada
caracter = input("Ingrese un carácter: ")

# Procesamiento Y Salida
if caracter in "aeiouAEIOU":
    print("vocal")
elif caracter in "qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM":
    print("consonante")
else:
    print("otro")