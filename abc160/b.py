Num = int(input())

ans = 0

val = int(Num / 500)
ans += val * 1000
val = int((int(Num % 500)) / 5)
ans += val * 5

print(ans)