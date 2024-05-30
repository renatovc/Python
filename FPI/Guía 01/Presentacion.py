# Entrada
nombre = input("Nombre: ")
año_de_nacimiento = input("Año de nacimiento: ")

# Procesamiento
nombre = nombre.title()

nombre_apellido_separado = nombre.split(" ", 1)
nombre_solo = nombre_apellido_separado[0]

nombre_solo = str(nombre_solo)

# Se realiza el calculo respectivo de edad
año_de_nacimiento = int(año_de_nacimiento)
edad = 2023 - año_de_nacimiento
edad_string = str(edad)

# Salida
print("Hola, " + nombre_solo + ". " "Tienes", edad_string, "años.")