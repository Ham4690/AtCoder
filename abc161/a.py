def swp(x, y):
  swp = x
  x = y
  y = swp
  return x, y
  

A, B, C = map(str, input().split())

A, B = swp(A, B)
A, C = swp(A, C)

print(A + ' ' + B + ' ' + C)