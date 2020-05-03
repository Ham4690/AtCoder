N, K = map(int, input().split())
A_ans = [1 for i in range(N)]
for i in range(K):
    d = int(input())
    if d > 1 :
        A = list(map(int, input().split()))
        for j in range(len(A)):
            if A_ans[A[j]-1] == 1 :
                A_ans[A[j]-1] = 0
    else:
        A = int(input())
        if A_ans[A-1] == 1 :
            A_ans[A-1] = 0

print(sum(A_ans))
 
