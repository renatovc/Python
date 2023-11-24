# Bloque de Definiciones
def contar_vocales(text):
  vocals = "aeiouáéíóúAEIOUÁÉÍÓÚäëïöüÄËÏÖÜ"
  count = 0
  for char in text:
    if char in vocals:
      count += 1
  return count