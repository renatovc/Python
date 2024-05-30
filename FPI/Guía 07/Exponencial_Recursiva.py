def exp(base, exponente):
  if exponente == 0:
    return 1
  elif exponente % 2 == 0:
    i = exp(base, exponente // 2)
    return i * i
  else:
    return base * exp(base, exponente - 1)