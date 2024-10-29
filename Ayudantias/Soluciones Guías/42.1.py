# Entrada
password = input("Ingrese su pass: ")

# Procesamiento y Salida
contieneMinuscula = False
contieneMayuscula = False
contieneLetra = False
contieneDigito = False
contieneComa = False
contienePuntoComa = False

abcedario = "abcdefghijklmnopqrstuvwxyz"
digitos = "0123456789"

if len(password) == 8:
    for caracter in password:
        if caracter in abcedario:
            contieneMinuscula = True
            contieneLetra = True
        elif caracter in abcedario.upper():
            contieneMayuscula = True
            contieneLetra = True
        elif caracter in digitos:
            contieneDigito = True
        elif caracter == ",":
            contieneComa = True
        elif caracter == ";":
            contienePuntoComa = True

    # Salidas
    if not contieneMinuscula:
        print("Debe tener al menos una minúscula.")

    if not contieneMayuscula:
        print("Debe tener al menos una mayúscula.")

    if not contieneLetra:
        print("Debe tener al menos una letra.")

    if not contieneDigito:
        print("Debe tener al menos un dígito.")

    if not contieneComa:
        print("Debe tener al menos una coma.")

    if not contienePuntoComa:
        print("Debe tener al menos una punto y coma.")
else:
    print("Debe tener 8 caracteres.")

# Salida
if contieneMinuscula and contieneMayuscula and contieneLetra and contieneDigito and contieneComa and contienePuntoComa:
    print("Su password cumple con todas las reglas.")