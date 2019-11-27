import math

A,B,X = map(int,input().split())

# A * N + B * d(N) yen 

check_num = [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]

if((A*1+B*1)>X):
    print(0)
else:
    flag = True
    for i in range(len(check_num)):
        if((A*check_num[i]+B*(i+2)) > X):
            i = i + 1
            flag = False
            break
    if(flag):
        print(10**9)
    else:
        Num = (X - B*i)/A
        if(isinstance(Num,int)):
            value = Num + 1
        else:
            value = math.ceil(Num)
        print(value-1)
