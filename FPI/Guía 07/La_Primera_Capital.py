def first_capital(text, index=0):
  if index < len(text):
    if text[index].isupper():
      return [text[index], index]
    else:
      return first_capital(text, index + 1)
  else:
    return ["", -1]