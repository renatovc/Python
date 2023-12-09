def power_set(s):
  def generate_power_set(current_set, remaining, result):
    result.append(current_set)

    for i, char in enumerate(remaining):
      generate_power_set(current_set + char, remaining[i + 1:], result)

  result = []

  generate_power_set('', sorted(s), result)

  return result