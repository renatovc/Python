# Entrada
sec_digitos = input("Ingrese una secuencia de digitos: ")

# Procesamiento
long_max = 0
long_act = 1

for i in range(1, len(sec_digitos)):
    if sec_digitos[i] > sec_digitos[i - 1]:
        long_act += 1
    else:
        if long_act > long_max:
            long_max = long_act
        long_act = 1

if long_act > long_max:
    long_max = long_act

# Salida
print(long_max)