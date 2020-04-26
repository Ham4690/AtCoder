import math

def calcConbination(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    return n + calcConbination(n-1)

N, M = map(int, input().split())
ans = 0
if N > 1 :
  ans += calcConbination(N-1)

if M > 1 :
  ans += calcConbination(M-1)

print(ans)