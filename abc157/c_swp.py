import sys
N, M = map(int, input().split())

C = []
S = []

for i in range(M):
    c, s = map(int, input().split())
    C.append(c)
    S.append(s)

for x in range(1000):
    keta = 1
    nx = x//10
    d = [x%10]


    while(nx):
        keta += 1
        d.append(nx%10)
        nx = nx // 10
    d = list(reversed(d))

    isOk = True
    
    for i in range(M):
        if( d[C[i]-1] != S[i-1] ):
            isOk = False

    if isOk :
        num = "".join(map(str, d))
        break

if isOk:
    print(num)
else:
    print(-1)