Tax = 1.08
n = int(input())
value = int(n/Tax)
flag = True
for i in range(2):
    check_value = (value+i)*Tax
    if(int(check_value) == n):
        print(value+i)
        flag = False
if flag:
    print(":(")