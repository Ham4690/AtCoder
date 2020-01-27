# (A1+..+AN-1 + x)/N <= M

n, k, m = map(int, input().split())

a = list(map(int, input().split()))
a_total = sum(a)
flag = True
for i in range(0,k+1):
    ans = (a_total + i) / n
    if ans >= m :
        flag = False 
        print(i)
        break
if flag:
    print(-1)

