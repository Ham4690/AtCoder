import numpy as np

N = int(input())

a = []
for i in range(N):
    a.append(int(input()))

if(N==1):
    print(a[0])
else:
    a_max = 0
    n_a_max = 0
    all_max = max(a)
    max_arg = np.argmax(a)

    if(max_arg!=0):
        a_max = max(a[:max_arg])
    if(max_arg!=N-1):
        n_a_max = max(a[max_arg+1:])

    if(a_max>=n_a_max):
        next_max = a_max
    else:
        next_max = n_a_max

    for i in range(N):
        if a[i]==all_max:
            print(next_max)
        else:
            print(all_max)
        