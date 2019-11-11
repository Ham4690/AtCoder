N = list(input())

ans = 0

N_len = len(N)
judge = True
if(N_len==1):
    print(int(N[0]))
else:
    for i in range(1,N_len):
        if int(N[0]) < int(N[i]):
            judge = False
            break
    
    if judge :
        for i in range(N_len):
            ans = ans + int(N[0])*10**i
    else :            
        for i in range(N_len):
            ans = ans + (int(N[0])+1)*10**i

    print(ans)
