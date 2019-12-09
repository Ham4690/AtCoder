import collections as c
import numpy as np

N,K = map(int,input().split()) 
A = list(map(int,input().split()))
A_c = c.Counter(A)
A_c = sorted(list(A_c.values()))
KindNum = len(A_c)
if KindNum < K:
    print(0)
else:
    ans = sum(A_c[:KindNum - K])
    print(ans)
    

