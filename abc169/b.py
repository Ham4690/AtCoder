import sys

N = int(input())
a_list = list(map(int, input().split()))

def inZero(nums):
  return 0 in nums

def isOverDigits(nums):
  digits = 0

  for i in range(len(nums)):
    digits += len(str(nums[i])) - 1

  if digits > 18:
    return True
  else:
    return False

def calcAns(nums):
  ans = 1
  for i in range(len(nums)):
    ans = ans * nums[i]
    if ans > 10**18 :
      return False
  return ans

if inZero(a_list):
  print(0)
  sys.exit()

ans = calcAns(a_list) 

if ans :
  print(ans)
else :
  print(-1)



