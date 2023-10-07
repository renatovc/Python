# Escriba su código acá
# ENTRADA
numero = ''
# PROCESAMIENTO
# Esta variable controla que el while siga o no.
valido = False

while not valido:
    valido = True
    # Pido el numero
    numero = input()
    # En caso que el string de entrada tenga un signo al inicio
    if numero[0] == '-' or numero[0] == '+':
        i = 1
        # Recorro el numero caracter a caracter
        while i < len(numero):
            # Si el caracter no está entre los posibles digitos
            if numero[i] not in '0123456789':
                # Imprimo el error
                print('Error de ingreso!')
                # Si encuentro algun problema cambio el valor de la variable
                # valido
                valido = False
                # Salgo del while
                i = len(numero)
            i = i + 1
    else:
        # Este caso es igual al anterior, solo que parto revisando desde 0
        i = 0
        # Recorro el numero caracter a caracter
        while i < len(numero):
            # Si el caracter no está entre los posibles digitos
            if numero[i] not in '0123456789':
                # Imprimo el error
                print('Error de ingreso!')
                # Si encuentro algun problema cambio el valor de la variable
                # valido
                valido = False
                # Salgo del while
                i = len(numero)
            i = i + 1

    if valido:
        # Convierto a flotante para mostrar la variable como número y no como string
        numero = float(numero)
        print('Se ha obtenido el número:', numero)
