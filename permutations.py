def permutations(l):
  if not l: return
  if len(l) == 1: yield (l[0],)
  else:
      for j in l:
          l2 = [i for i in l if i != j]
          for t in permutations(l2):
              yield (j,) + t
