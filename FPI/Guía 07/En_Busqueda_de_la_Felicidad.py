def is_happy(n):

  def sum_digit_square(num):
    return sum(int(digit)**2 for digit in str(num))

  visit = set()

  def happy(num):
    if num == 1:
      return True
    elif num in visit:
      return False
    else:
      visit.add(num)
      return happy(sum_digit_square(num))

  return happy(n)
