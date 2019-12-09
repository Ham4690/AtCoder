import numpy as np

def checkTestimony(honest, A_map, N):
    for i in range(N):
        for j in range(len(A_map[i])):
            Opponent = A_map[i][j][0] - 1
            OpJudge  = A_map[i][j][1]
            if honest[i] == 0:
                if honest[Opponent] == OpJudge:
                    return False 
            else:
                if honest[Opponent] != OpJudge:
                    return False 
    return True    

def setHonest (num, l):
    for i in range(len(l)):
        if (num >> i) & 1 == 1:
            l[i] = 1

N = int(input())
A_map = {}
ans = [0]
for i in range(N):
    A = int(input())
    if A > 0:
        for j in range(A):
            xy = list(map(int,input().split()))
            if i in A_map.keys():
                A_map[i].append(xy)
            else:
                A_map[i] = [xy]

for i in range(2**N):
    honest = [0] * N
    setHonest(i, honest)
    if checkTestimony(honest, A_map, N) :
        honestNum = honest.count(1)
        ans.append(honestNum)

print(max(ans))
