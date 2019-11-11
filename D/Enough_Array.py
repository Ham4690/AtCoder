
N,K = map(int,input().split())

a = list(map(float,input().split()))

s = []
s.append(a[0])
for i in range(1,N):
    s.append( s[i-1] + a[i])
print(s)

'''
count = 0
for i in range(0,N-1):
    for j in range(i+1,N+1):
        total = 0
        for k in range(i,j):
            total += a[k]
            if(total >= K):
                count += 1
                break
'''
count = 0
for i in range(0,N):
    for j in range(i,N):
        # print(i)
        # print(j)
        print(s[j]-s[i])
        if(j==i):
            if(a[i] >= K):
                count +=1
        elif(i==0 and j == N-1):
            if(a[])
        elif((s[j]-s[i])>= K):
            count += 1


print(count)