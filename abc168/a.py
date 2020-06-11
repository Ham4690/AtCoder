def iscall(num):
  if num == 2 or num == 4 or num == 5 or num == 7 or num == 9:
    return 'hon'
  elif num == 0 or num == 1 or num == 6 or num == 8:
    return 'pon'
  elif num == 3:
    return 'bon'

N = list(input())

ans = iscall(int(N[-1]))
print(ans)