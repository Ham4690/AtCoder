import sys

N = int(input())
a = list(map(int,input().split()))

if a[0] != a[len(a)-1]^a[1]:
    print('No')
    sys.exit()

for i in range(1,N-1):
    if a[i] != a[i-1]^a[i+1]:
        print('No')
        sys.exit()

if a[len(a)-1] != a[len(a)-2]^a[0]:
    print('No')
    sys.exit()

print('Yes')


    