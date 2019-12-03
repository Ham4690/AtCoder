N = int(input())
flag = False
if(N > 81):
    print("No")
else:
    for i in range(1,10):
        if (N % i == 0) and (N // i < 10):
            flag = True
            break
    if flag :
        print("Yes")
    else:
        print("No")