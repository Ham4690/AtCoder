import numpy as np
N = int(input())


t_l =np.array([[0.5 for i in range(N)] for j in range(N)])

for i in range(N):
    A = int(input())
    for j in range(A):
        x,y = map(int,input().split())
        t_l[i][x-1] = y

t_l = (t_l - 0.5) * 2
print(t_l)
print(t_l[:][1])

# Num = 2**N - 1
# ans = list(bin(Num)[2:])

# while 1 :
#     if check(ans,t_l,N):
#         ans.count('1')
#         exit()
    
#     Num = Num - 1
#     ans = list(bin(Num)[2:])
    

