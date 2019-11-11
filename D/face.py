N,K = map(int,input().split())
S = list(input())
# print(S)

score = 0

for i in range(1,N-1):
    if S[i-1]!=S[i] and S[i+1]!=S[i] :
        S[i] = S[i-1]
        K -= 1
        if K <= 0:
            break

if(K!=0):
    for i in range(1,N):
        if(S[i-1]!=S[i]):
            S[i] = S[i-1]
            K -= 1
            if (K<=0):
                break

for i in range(1,N):
    if S[i-1] == S[i]:
        score += 1

print(S)
print(score)