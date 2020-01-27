H = int(input())

count = 0
enemy = H
ans = 0

while(enemy >= 1):
    enemy /= 2
    count += 1

for i in range(count):
    ans += 2**(count-1)
    count -= 1

print(ans)