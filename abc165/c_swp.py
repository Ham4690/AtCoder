N, M, Q = map(int, input().split())
in_list = []
ans = 0
a = []
b = []
c = []
d = []
for i in range(Q):
    a_in, b_in, c_in, d_in = list(map(int, input().split()))
    a.append(a_in)   
    b.append(b_in)   
    c.append(c_in)   
    d.append(d_in)   

def dfs(A) :
    if len(A) == N+1:
        nowScore = 0
        print(A)
        for i in range(Q):
            if A[b[i]] - A[a[i]] == c[i]:
                nowScore += d[i]
        ans = max(ans, nowScore)

    A.append(A[-1])
    while A[-1] <= M:
        dfs(A)
        A[-1] += 1

test = [1]
dfs(test)
print(ans)