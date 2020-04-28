
N, K = map(int, input().split())

if K == 1:
  print(0)
else:
  a = N % K
  if a > K-a:
    print(K-a)
  else:
    print(a)
