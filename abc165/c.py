def check(A, B, C):
    if B - A <= C:
        return True
    else:
        return False


N, M, Q = map(int, input().split())
in_list = []
A = [0 for i in range(N)]
ans = 0
for i in range(Q):
    A, B, C, D = list(map(int, input().split()))
    in_list.append([A,B,C,D])



print(in_list)