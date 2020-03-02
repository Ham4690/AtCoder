N, M = map(int, input().split())

ans = [0 for i in range(N)]
isTerms = [0 for i in range(N)]
jadge = True

for i in range(M):
    s, c = map(int, input().split())
    if( ans[s-1] != c and isTerms[s-1] != 0):
        jadge = False
    elif( s == 1 and c == 0):
        jadge = False
    else:
        ans[s-1] = c
        isTerms[s-1] = 1

if( N != 1 and ans[0] == 0 and jadge):
    ans[0] = 1

if( N == 1 and ans[0] == 0):
    jadge = True

if jadge:
    if(N==1):
        print(ans[0])
    else:
        for i in range(N-1):
            print(ans[i] ,end = "")
        print(ans[i+1])
else:
    print(-1)