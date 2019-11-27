####kk
# coding: utf-8
# Your code here!

A, B, X = map(int, input().split())
min_num = 0
max_num = pow(10,9)
num = pow(10,9)

while True:
    tmp = A * num + B * len(str(num))
    if num == 0:
        print(0)
        break
    elif min_num + 2 <= max_num:
        if X >= tmp:
            min_num = num
        else:
            max_num = num
        num = (min_num + max_num) // 2
    else:    
        if X >= tmp:
            print(num)
            break