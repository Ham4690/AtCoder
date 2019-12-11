N = int(input())
A_map = {}

# input
for i in range(N):
    A = int(input())
    if A > 0:
        for j in range(A):
            xy = list(map(int,input().split()))
            if i in A_map.keys():
                A_map[i].append(xy)
            else:
                A_map[i] = [xy]
ans = 0

for bits in range(1,2**N):
    honest = True
    for i in range(1,N+1):
        if not (bits & (1 << (i-1))): continue

        if i in A_map.keys():
            for a in A_map[i]:   
                if ((bits >> (a[0] -  1)) & 1) ^ a[1] : honest = False
    if honest : 
        ans = max(ans, bin(bits).count('1'))

print(ans)
