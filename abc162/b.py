def isFizzBuzz (N):
  if N % 15 == 0 :
    return 0
  elif N % 3 == 0:
    return 0
  elif N % 5 == 0:
    return 0
  else:
    return N

N = int(input())
ans = 0
for i in range(1,N+1):
  ans += isFizzBuzz(i)

print(ans)
