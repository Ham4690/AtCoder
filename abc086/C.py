def existCheck(x,y,x_before,y_before):
   exist = False

   if (x_before + 1 == x and y_before == y) \
   or (x_before - 1 == x and y_before == y) \
   or (x_before == x and y_before + 1 == y) \
   or (x_before == x and y_before - 1 == y):
       exist = True

   return exist

N = int(input())

t_l = []
x_l = []
y_l = []

t,x,y = map(int,input().split())
t_before = t
x_before = x
y_before = y

existFlag = True

for i in range(1,N):
    t,x,y = map(int,input().split())

    if existCheck(x,y,x_before,y_before) == False:
        existFlag = False
        break
    t_before = t
    x_before = x
    y_before = y

if existFlag :
    print('Yes')
else:
    print('No')
   