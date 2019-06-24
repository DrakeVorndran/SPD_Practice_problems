def convert(number):
    factors = [number]
    for i in range(1, number//2 + 1):
      if number % i == 0:
        factors.append(i)
    cases = {
      3: 'Pling',
      5: 'Plang',
      7: 'Plong',
    }
    output = ''
    for i, word in cases.items():
      if i in factors:
        output += word
    if output:
      return output
    return str(number)


print(convert(7))
