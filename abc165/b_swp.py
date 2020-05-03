x = int(input())
ans = 0
a = 100

while a < x :
    a += a//100
    ans += 1

print(ans)
