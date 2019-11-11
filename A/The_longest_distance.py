import math

N = int(input())

x_y = [[0 for i in range(2)] for j in range(N)]
# print(x_y)
for i in range(N):
    x_y[i][0],x_y[i][1] = map(int,input().split())
    # print(x_y[i])

max_distance = 0

for i in range(N):
    for j in range(i+1,N):
        if(max_distance < math.sqrt((x_y[i][0]-x_y[j][0])**2 + (x_y[i][1]-x_y[j][1])**2)):
            max_distance = math.sqrt((x_y[i][0]-x_y[j][0])**2 + (x_y[i][1]-x_y[j][1])**2)

print("%f"%max_distance)