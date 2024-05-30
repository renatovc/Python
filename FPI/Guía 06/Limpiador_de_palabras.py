# Bloque Definiciones
def limpiar_palabras(texto):
  palabras_limpias = ""

  for i in texto:
    if i.isalpha() or i.isdigit() or i.isspace():
      palabras_limpias += i

  palabras = palabras_limpias.split(" ")

  return palabras