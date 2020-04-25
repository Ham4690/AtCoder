N = int(input())
BossNumsList = list(map(int, input().split()))
SubNumsList = [0 for i in range(N)]

for BossNum  in BossNumsList :
  SubNumsList[BossNum-1] += 1

for i in range(N):
  print(SubNumsList[i])