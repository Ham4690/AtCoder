N = int(input())
points = []
total = 0

for i in range(N):
    points.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        total+=((points[i][0]-points[j][0])**2+(points[i][0]-points[j][0])**2)**0.5

print(total/N)



