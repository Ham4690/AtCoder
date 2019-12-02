N = int(input())
S = list(map(int,input()))
count = 0
for i in range(10):
    if i in S[:-2] :
        v1 = S[:-2].index(i)
        for j in range(10):
            if j in S[v1+1:-1] :
                v2 = S[v1+1:-1].index(j) + v1 + 1
                for k in range(10):
                    if k in S[v2+1:] :
                        count += 1
print(count)





