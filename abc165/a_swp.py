import math

K = int(input())
a, b = map(int, input().split())

if a <= (math.floor(b/K) * K):
    print('OK')
else:
    print('NG')