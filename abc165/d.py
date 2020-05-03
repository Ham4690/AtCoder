import math
A, B, N = map(int, input().split())

if N < B-1 :
    div_num = N
else:
    div_num = B-1

print( math.floor(( A*(div_num % B)/B )) )

