# Bloque Importaciones
from random import choice, randint

# Bloque Definiciones
def position_list(size):
  list = []
  for i in range(size):
    list.append(i)
  return list


def determine_quantites(size):
  mayus_cant = -1
  minus_cant = -1
  special_cant = -1
  numbers_cant = -1

  while (mayus_cant == minus_cant == special_cant == numbers_cant):
    size_copy = size
    minus_cant = randint(1, size_copy - 3)
    size_copy = size_copy - minus_cant
    special_cant = randint(1, size_copy - 2)
    size_copy = size_copy - special_cant
    numbers_cant = randint(1, size_copy - 1)
    mayus_cant = size - (minus_cant + special_cant + numbers_cant)
  return [mayus_cant, minus_cant, special_cant, numbers_cant]


def generate_password_aux(size):
  mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  password = []
  for i in range(size):
    password.append(choice(mayus))

  return password


def gen_pw(max, min=8):
  if min > max:
    return ""

  mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  minus = mayus.lower()
  special = "?!@#$%^&*"
  numbers = "0123456789"

  size = choice([min, max])

  position = position_list(size)

  quantiti = determine_quantites(size)

  mayus_cant = quantiti[0]
  minus_cant = quantiti[1]
  symbols_cant = quantiti[2]
  numbers_cant = quantiti[3]

  password = generate_password_aux(size)

  for i in range(minus_cant):
    pos = choice(position)
    position.remove(pos)
    password[pos] = choice(minus)

  for i in range(symbols_cant):
    pos = choice(position)
    position.remove(pos)
    password[pos] = choice(special)

  for i in range(numbers_cant):
    pos = choice(position)
    position.remove(pos)
    password[pos] = choice(numbers)

  password = "".join(password)

  return password
