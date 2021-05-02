N = int(input())
abilities_li = []
A_list = []
B_list = []
C_list = []
D_list = []
E_list = []
A_max = 0
B_max = 0
C_max = 0
D_max = 0
E_max = 0

max_team = 0
for i in range(N):
    A, B, C, D, E = map(int, input().split())
    abilities_li.append([A, B, C, D, E])
    A_max = max(A_max, A)
    B_max = max(B_max, B)
    C_max = max(C_max, C)
    D_max = max(D_max, D)
    E_max = max(E_max, E)

    A_list.append(A)
    B_list.append(B)
    C_list.append(C)
    D_list.append(D)
    E_list.append(E)

indexes = []
A_indexes = [i for i, x in enumerate(A_list) if x == A_max]
for i in A_indexes :
    indexes.append(i)

B_indexes = [i for i, x in enumerate(B_list) if x == B_max]
for i in B_indexes :
    indexes.append(i)

C_indexes = [i for i, x in enumerate(C_list) if x == C_max]
for i in C_indexes :
    indexes.append(i)

D_indexes = [i for i, x in enumerate(D_list) if x == D_max]
for i in D_indexes :
    indexes.append(i)

E_indexes = [i for i, x in enumerate(E_list) if x == E_max]
for i in D_indexes :
    indexes.append(i)

for i in A_indexes :
    indexes.append(i)

for i in range(N):
    if(max(abilities_li[i]) < max_team) :
        continue
    for j in range(i+1, N):
        if(max(abilities_li[j]) < max_team) :
            continue
        for k in range(j+1, N):
            if(max(abilities_li[k]) < max_team) :
                continue
            max_li = []
            max_li.append(max(A_list[i], A_list[j], A_list[k]))
            max_li.append(max(B_list[i], B_list[j], B_list[k]))
            max_li.append(max(C_list[i], C_list[j], C_list[k]))
            max_li.append(max(D_list[i], D_list[j], D_list[k]))
            max_li.append(max(E_list[i], E_list[j], E_list[k]))
            max_team = max(max_team, min(max_li))

print(max_team)




