#2<=N<=100
#1<=W_i<=100

N = int(input())

weight_list = list(map(int,input().split()))

minWeight = 1000
for i in range(N):
    S_1=0
    S_2=0
    for j in range(i):
       S_1 += weight_list[j]
    for j in range(i,N):
       S_2 += weight_list[j]

    if(minWeight>(abs(S_1 - S_2))):
        minWeight = abs(S_1-S_2)

print(minWeight)