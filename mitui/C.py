
x = int(input())   

count = int(x/100)
if 100*count <= x and x <= 105*count:
    print(1)
else:
    print(0)