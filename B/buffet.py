N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

total = 0


for i in range(len(A)):
    total += B[A[i]-1]
    if i!=0 and A[i-1]+1 == A[i]:
        total += C[A[i-1]-1]

print(total)

# print(N)
# print(A)
# print(B)
# print(C)
