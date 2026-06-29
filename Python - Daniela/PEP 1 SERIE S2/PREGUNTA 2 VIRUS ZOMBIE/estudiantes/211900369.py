# Entrada
muestra_adn = input("Ingrese la muestra de ADN: ")
vacuna = input("Ingrese la vacuna: ")

# Procesamiento
adn_infectado = muestra_adn[9:14]

# Obtener secuencia emparejamiento ADN infectado
sec_emparejamiento = ""
for base in adn_infectado:
    if base == "A":
        sec_emparejamiento += "T"
    elif base == "T":
        sec_emparejamiento += "A"
    elif base == "C":
        sec_emparejamiento += "G"
    elif base == "G":
        sec_emparejamiento += "C"

# Verificar compatibilidad vacuna
count_emparejamiento = vacuna.count(sec_emparejamiento)

# Salida
if count_emparejamiento % 2 == 1:
    print("CORRECTA")
else:
    print("INCORRECTA")