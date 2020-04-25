N, M = map(int, input().split())
workDays = list(map(int,input().split()))
sumDays = sum(workDays)

if sumDays > N :
  print(-1)
else:
  print(N-sumDays)
