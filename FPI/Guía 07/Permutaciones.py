def permutations(string):
  if len(string) == 1:
    return [string]

  result = []

  for i, char in enumerate(string):
    remaining = string[:i] + string[i + 1:]
    for perm in permutations(remaining):
      result.append(char + perm)

  return sorted(result)