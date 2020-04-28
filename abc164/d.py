S = list(input())

S_len = len(S)
ans = 0

for i in range(S_len - 3):
  for j in range(i+3, S_len+1):
    num = int("".join(map(str, S[i:j])))
    if num % 2019 == 0:
      ans += 1

print(ans)