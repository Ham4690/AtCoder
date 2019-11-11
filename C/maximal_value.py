N = int(input())
B = list(map(int,input().split()))

A = [0 for i in range(N)]
A[0] = B[0]
A[1] = B[0]

for i in range(1,len(B)):
    if(B[i] < A[i]):
        A[i] = B[i]
    
    A[i+1] = B[i]

print(sum(A))


