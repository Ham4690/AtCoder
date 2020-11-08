N = input()
N_list = [int(i) for i in N]
N_list = list(map(lambda x: x%3 , N_list))
# print(N_list)
check = sum(N_list)%3
one_cnt = N_list.count(1)
two_cnt = N_list.count(2)

if check == 0:#余りが0の時
    print(0)

elif check == 1 :#余りが1の時
    if one_cnt >= 1:
        if len(N_list) == 1:
            print(-1)
        else: 
            print(1)
    else:
        if len(N_list) == 2 :
            print(-1)
        else:
            print(2)
else : #余りが2の時
    if two_cnt >= 1:
        if len(N_list) == 1 :
            print(-1)
        else: 
            print(1)
    else:
        if len(N_list) == 2:
            print(-1)
        else:
            print(2)




