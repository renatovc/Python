# Bloque Definiciones
def is_palindrome(text):
  text = text.lower()
  for i in range(len(text)):
    if text[i] == "Á":
      text = text.replace("Á", "A")
    elif text[i] == "É":
      text = text.replace("É", "E")
    elif text[i] == "Í":
      text = text.replace("Í", "I")
    elif text[i] == "Ó":
      text = text.replace("Ó", "O")
    elif text[i] == "Ú":
      text = text.replace("Ú", "U")
    elif text[i] == "Ú":
      text = text.replace("Ü", "U")
    elif text[i] == "á":
      text = text.replace("á", "a")
    elif text[i] == "é":
      text = text.replace("é", "e")
    elif text[i] == "í":
      text = text.replace("í", "i")
    elif text[i] == "ó":
      text = text.replace("ó", "o")
    elif text[i] == "ú":
      text = text.replace("ú", "u")
    elif text[i] == "ü":
      text = text.replace("ü", "u")

  text_cleaned = ""

  for x in text:
    if x.isalpha():
      text_cleaned += x

  return text_cleaned == text_cleaned[::-1]