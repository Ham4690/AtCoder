import math

def getPosition(Num, n, i):
    Num_buff = Num[i:]
    # print(Num_buff)
    Num_buff.sort()
    return Num_buff.index(n)



N = int(input())
P = list(map(int,input().split())) 
Q = list(map(int,input().split())) 

a = 0
b = 0

# print(P)
# print(Q)
# print("---")

for i in range(N):
    a += (getPosition(P, P[i], i))*math.factorial(N-(i+1)) 
    b += (getPosition(Q, Q[i], i))*math.factorial(N-(i+1)) 
a += 1
b += 1
if a > b:
    print(a-b)
else:
    print(b-a)
# print(a)
# print(b)