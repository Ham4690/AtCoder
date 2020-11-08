N = int(input())
A = list(map(int, input().split()))
ans = 0
ans_cnt = 0
for i in range(2, max(A)+1) : 
    cnt = 0
    for j in range(len(A)):
        if(A[j] % i == 0):
            cnt = cnt + 1
    
    if( cnt > ans_cnt ):
        ans = i 
        ans_cnt = cnt

print(ans)
        

    



