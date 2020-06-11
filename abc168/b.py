def output(list_str, len):
  for i in range(len):
    print(list_str[i], end="")

K = int(input())
S = list(input())

if len(S) <= K :
  output(S, len(S))
  print()
else:
  output(S, K)
  print("...")