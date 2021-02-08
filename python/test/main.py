s = 9**9 + 3**21 - 7
counter0 = 0
while s:
  if s % 3 == 0: counter0 += 1
  s //= 3
print(counter0)

