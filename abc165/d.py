import math

A, B, N = map(int, input().split())

ans = math.floor((A)/B) - A * math.floor(1/B)
MaxAns = ans
for x in range(N, 2, -1):
    ans_swp = math.floor((A*x)/B) - A * math.floor(x/B)
    if MaxAns < ans_swp:
        MaxAns = ans_swp

    if ans > ans_swp:
        break
    else:
        ans = ans_swp

print(MaxAns)
