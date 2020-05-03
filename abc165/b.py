def calc(x):
    return int(x * 1.01)

X = int(input())
val = 100
y = 0
while True:
    if val >= X:
        print(y)
        break
    val = calc(val)
    y += 1
