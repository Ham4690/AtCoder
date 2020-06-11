import math

def toTimeMin(hour, min):
  time = 0
  time += hour * 60
  time += min

  return time

def hourHandPosition(time):
  return 0.5 * time

def minHandPosition(time):
  t = time % 60
  return 6 * t 

A, B, H, M = map(int, input().split())

time = toTimeMin(H, M)

pA = hourHandPosition(time)
print(pA)
pB = minHandPosition(time)
print(pB)

angle = max(pA, pB) - min(pA, pB)

c = A**2 + B**2 - (2 * A * B * math.cos(angle))
print(math.sqrt(c))

