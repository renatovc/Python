# Bloque Definiciones
def str_to_int(value):
  str_sep = value.strip()

  if not str_sep:
    raise ValueError(f"No se puede convertir {value}")

  evaluate = 0
  is_negative = False
  if str_sep[0] == "-":
    is_negative = True

  index = 0

  if is_negative:
    index = 1

  for number in str_sep[index:]:
    if number < "0" or number > "9":
      raise ValueError(f"No se puede convertir {value}")

    digits = "0123456789"
    digits = digits.index(number)
    evaluate = evaluate * 10 + digits

  if is_negative:
    evaluate = -evaluate

  return evaluate


def int_to_str(value):
  if value == 0:
    return "0"

  digits = "0123456789"
  result = []
  is_negative = False

  if value < 0:
    is_negative = True
    value = abs(value)

  while value != 0:
    calculation = value % 10
    number = digits[calculation]
    result.append(number)
    value = value // 10

  if is_negative:
    result.append("-")

  result.reverse()

  result_reverse = "".join(result)

  return result_reverse