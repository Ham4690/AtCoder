N, M, K = map(int, input().split())
A = []
B = [] 
C = []
D = []

friendCandidate = [[1 for i in range(N)] for j in range(N)]

ans = [N-1 for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    friendCandidate[a-1][b-1] = 0
    friendCandidate[b-1][a-1] = 0
    ans[a-1] -= 1
    ans[b-1] -= 1

for i in range(K):
    c, d = map(int, input().split())
    friendCandidate[c-1][d-1] = -1
    friendCandidate[d-1][c-1] = -1
    ans[c-1] -= 1
    ans[d-1] -= 1

# for i in range(N-1):
#     print(str(ans[i]) + ' ',end="")
# print(str(ans[i+1]))
for i in range(N):
