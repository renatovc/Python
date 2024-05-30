def buscar(num):
  for i in range(1, num + 1):
    nombre_arch = f"{i}.txt"
    with open(nombre_arch, "r", encoding="utf-8") as archivo:
      cont = archivo.readline().strip()
      if cont == "7.0":
        return nombre_arch