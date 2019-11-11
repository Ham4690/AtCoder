N = int(input())

ball = [[0 for i in range(2)] for j in range(N)]

for i in range(N):
    ball[i][0],ball[i][1] = map(int,input().split())

print(ball)
ball.sort(reverse = True)
print(ball)
minCost = N

p = ball[0][0]
q = ball[0][1]
max_match_x = 0
max_match_y = 0

for i in range( max(ball[0][0],ball[0][1]) ):
    Cost = 1

    print('p:%d,q:%d'%(p,q))

    for j in range(1,N):
        if (ball[j][0] != ball[j-1][0] - p) or (ball[j][1] != ball[j-1][1] - q):
            Cost += 1
    
    if(minCost > Cost):
        minCost = Cost
    print('Cost:'+str(Cost))

    p-=1
    q-=1

print(minCost)
