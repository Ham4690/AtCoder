H, A = map(int, input().split())
skills = list(map(int,input().split()))

if(sum(skills) >= H):
    print("Yes")
else:
    print("No")
