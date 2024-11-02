# Entrada
batallas = input("Batallas: ")
primer_bando = input("Primer bando: ")
segundo_bando = input("Segundo bando: ")

# Procesamiento
batallas = batallas.split("-")

count_primer_bando = 0
count_segundo_bando = 0

i = 0
while i < len(batallas):
    count_primer_bando += batallas[i].count(primer_bando)
    count_segundo_bando += batallas[i].count(segundo_bando)
    i += 1

# Salida
if count_primer_bando < count_segundo_bando:
    print("Gana el bando", segundo_bando)
elif count_primer_bando > count_segundo_bando:
    print("Gana el bando", primer_bando)
else:
    print("Empate")