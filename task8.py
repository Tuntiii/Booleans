def lone_sum(a, b, c):
  listt=[a,b,c]
  summ=0

  d=[listt.count(a), listt.count(b), listt.count(c)]

  for i in range(0,3):
    if d[i] > 1:
      continue
    else:
      summ+=listt[i]

  return summ
