N, M = map(int, input().split())
H = list(map(int, input().split()))
A = []
B = []
ans = [1 for i in range(N)]
for i in range(M): 
    a, b = map(int, input().split())
    if H[a-1] < H[b-1]:
        # print()
        # print("bad")
        # print(str(a))
        ans[a-1] = 0
    elif H[a-1] == H[b-1]:
        ans[a-1] = 0
        ans[b-1] = 0

    else:
        ans[b-1] = 0

# print(ans)
print(sum(ans))