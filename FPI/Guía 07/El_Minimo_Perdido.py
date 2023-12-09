def find_min_missing(lista, start=0):
  if not lista or start < lista[0]:
    return start
  else:
    return find_min_missing(lista[1:], start + 1)