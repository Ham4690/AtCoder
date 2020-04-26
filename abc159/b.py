def isPalindrome(words ,start, end):
  i = start - 1
  j = end - 1
  while i < j :
    if words[i] != words[j]:
      return False
    i+=1
    j-=1

  return True

S = list(input())
N = len(S) #words length

if isPalindrome(S ,1, N) and isPalindrome(S, 1, int((N-1)/2)) and isPalindrome(S, int((N+3)/2), N) :
  print('Yes')
else:
  print('No')
