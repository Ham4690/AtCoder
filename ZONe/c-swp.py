N = int(input())
abilities_li = []
A_list = []
B_list = []
C_list = []
D_list = []
E_list = []
for i in range(N):
    A, B, C, D, E = map(int, input().split())
    A_list.append(A)
    B_list.append(B)
    C_list.append(C)
    D_list.append(D)
    E_list.append(E)



max_li = []
max_li.append(max(A_list))
max_li.append(max(B_list))
max_li.append(max(C_list))
max_li.append(max(D_list))
max_li.append(max(E_list))

print(min(max_li))




