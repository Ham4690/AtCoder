K, N = map(int, input().split())
A = list(map(int, input().split()))

distA = []

for i in range(N-1):
  distA.append( A[i + 1] - A[i] )
distA.append(A[0] + (K - A[N-1]) )
print(sum(distA) - max(distA))




