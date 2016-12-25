def listPosition(word):
  """Return the anagram list position of the word"""
  if len(word) == 1: return 1
  pos = 0
  for c in set(word):
      if c < word[0]:
            letters = list(word)
            letters.remove(c)
            pos += arrangements(letters)
  pos += listPosition(word[1:])
  return pos
        

def arrangements(letters):
    a = sorted(letters)
    n = factorial(len(letters))
    rep = 1
    last = '~'
    for c in a:
        if c == last: rep += 1
        elif rep > 1:
            n /= factorial(rep)
            rep = 1
            last = c
        else:
            last = c
    if rep > 1: n /= factorial(rep)
    return n

def factorial(n):
    f = 1
    for p in range(1, n + 1): f *= p
    return f
