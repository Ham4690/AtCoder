
#P :time a-b
#Q :time b-c
#R :time c-1

#1<=P,Q,R <=100
timelist = [0 for i in range(3)]

timelist[0],timelist[1],timelist[2] = map(int,input().split())
time = 200
for i in range(3):
    for j in range(i+1,3):
        if( time > (timelist[i]+timelist[j]) ):
            time = (timelist[i]+timelist[j])
print(time)

