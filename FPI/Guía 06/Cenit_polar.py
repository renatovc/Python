# Bloque Definiciones
def cypher_text(text, key):
  if len(key) != 2 or len(key[0]) != len(key[1]):
    return -1

  combinated = key[0] + key[1]

  for x in range(len(combinated)):
    for y in range(x + 1, len(combinated)):
      if combinated[x] == combinated[y]:
        return -1

  cyphered = ""
  for letter in text:
    aux = 0

    minus = letter.lower()
    is_mayus = letter.isupper()

    for i in range(len(key[0])):
      if minus == key[0][i]:
        if is_mayus:
          aux = key[1][i].upper()
        else:
          aux = key[1][i]

      elif minus == key[1][i]:
        if is_mayus:
          aux = key[0][i].upper()
        else:
          aux = key[0][i]

    if aux:
      cyphered += aux
    else:
      cyphered += letter

  return cyphered
