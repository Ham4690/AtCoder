N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
isOk = True
judge_border = 1/(4 * M) * sum(A)
for i in range(M):
  if A[i] < judge_border:
    isOk = False
    break

if isOk :
  print('Yes')
else:
  print('No')
