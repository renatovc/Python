# Entrada, Procesamiento y Salida
clics_totales = int(input("Ingrese la cantidad de clics: "))

#Variables para el procesamiento
clic_usuarios = []
likes = 0
clics_actuales = 0

# Solicitar los clics de cada usuario
i = 0
while i < clics_totales:
    clics_por_usuario = int(input("Ingrese el ID del usuario que hizo clic: "))
    clic_usuarios.append(clics_por_usuario)
    i += 1

# Procesamos los clics para contar likes
for i in range(len(clic_usuarios)):
    if i == 0 or clic_usuarios[i] != clic_usuarios[i - 1]:
        if clics_actuales % 2 != 0:
            likes += 1
        clics_actuales = 1
    else:
        clics_actuales += 1

if clics_actuales % 2 != 0:
    likes += 1

# Imprimimos cantidad de likes
print(likes)