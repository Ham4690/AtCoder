import copy
N = int(input())
li = list(map(int,input().split()))
ans = copy.copy(li)
ans.sort()

count = 0
judge = True

for i in range(N-1):
    if (li[i] != ans[i]):
        count = count + 1
        if(count > 2):
            judge = False
            break

if(judge):
    print('YES')
else:
    print('NO')