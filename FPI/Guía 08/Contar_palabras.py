def readfile(nombre_archivo):
  with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()
  return contenido
  
def count_words(contenidos):
  def clean_text(text):
    return "".join(c.lower() for c in text if c.isalpha() or c.isspace())

  clean_content = clean_text(contenidos)
  word = clean_content.split()
  return len(word)