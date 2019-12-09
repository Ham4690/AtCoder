
def numConvertHalf(numbers):
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i]/2)

def checkEven(numbers):
    for i in range(len(numbers)):
        if(numbers[i] % 2 == 1):
            return False
    return True

N = int(input())
numbers = list(map(int,input().split()))
count = 0
while checkEven(numbers):
    numConvertHalf(numbers)
    count += 1
print(count)