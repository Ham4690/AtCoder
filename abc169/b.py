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
  return ans

if inZero(a_list):
  print(0)
  sys.exit()

ans = calcAns(a_list) 

if ans > 10**18 :
  print(-1)
else :
  print(ans)



