import collections
import numpy as np
N,K = map(int,input().split())
A = [int(x) for x in input().split()]
B=collections.Counter(A)
print(B)
print(B.values())
C=sorted(list(B.values()))
print(C)
if len(C)<=K:
  answer=0
else:
  answer=np.cumsum(C)[len(C)-K-1]
print(answer)