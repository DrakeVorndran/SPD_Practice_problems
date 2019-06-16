def is_isogram(string):
  accepted_chars = [' ', '-']
  string = string.lower()  
  for i in range(len(string)-1):
    if string[i] not in accepted_chars:
      for second_char in string[i + 1:]:
        if string[i] == second_char:
          return False
  return True

