N = int(input())
a_li = list(map(int,input().split()))
b_li = list(map(int,input().split()))

total = 0

for i in range(N):
    if(a_li[i] <= b_li[i]):
        total = total + a_li[i]
        b_li[i] = b_li[i] - a_li[i]
        if(a_li[i+1] <= b_li[i]):
            total = total + a_li[i+1]
            a_li[i+1] = 0
        else:
            total = total + b_li[i]
            a_li[i+1] = a_li[i+1] - b_li[i]
    else:
        total = total + b_li[i]

print(total)

