N = int(input())
ans = 0
for i in range(N):
    A, B = map(int,input().split())
    A_sum = (A*(A+1))/2
    B_sum = (B*(B+1))/2
    ans = ans + int(B_sum - A_sum + A)

print(ans)
