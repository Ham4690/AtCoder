a,b = map(int,input().split())

if(a > b):
    d = a-b
else:
    d = b-a

if(d%2 == 0):
    if(a > b):
        print(a - int(d/2))
    else:
        print(b - int(d/2))


else:
    print('IMPOSSIBLE')
