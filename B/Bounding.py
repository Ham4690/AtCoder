
N,X = map(int,input().split())
L_list = [0 for i in range(N)]

L = list(map(int,input().split()))

D = 0
count = 0

if D <= X :
    count += 1

for i in range(N):
    D_next = D + L[i]
    if(D_next <= X):
        count += 1
    D = D_next

print(count)