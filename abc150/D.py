N, M = map(int,input().split())
a = list(map(int,input().split()))

count = 0

for i in range(N):
    flag = True
    while flag:
        p = 0
        x = a[i]*(p+0.5)

        if x > M :
            flag = False

        if x >= 0 and x.is_integer() : 
            count += 1
            flag = False
        p += 1

print(count)