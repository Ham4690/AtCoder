a,b = input().split()
ans = pow(int(a + b), 0.5)
ansInt = int(ans)

if (ans - ansInt) == 0 :
    print('Yes')
else:
    print('No')
