in_num = list(input())
N = list(map(int,in_num))
N = list(map(lambda x: x%3, N))

if len(N) == 2 and (N.count(1) == 2 or N.count(2) == 2 ) :
    print(-1)
elif len(N) == 1 and (N.count(1) == 1 or N.count(2) == 1 ):
    print(-1)
else:
    one_cnt = N.count(1) 
    two_cnt = N.count(2)

    if(two_cnt==0):
        print(one_cnt % 3)
    elif(one_cnt==0):
        print(two_cnt % 3)
    else:
        if two_cnt > one_cnt :
            cnt = two_cnt - one_cnt
        else:
            cnt = one_cnt - two_cnt

        ans_1 = cnt % 3

        one_cnt = N.count(1) % 2
        two_cnt = (N.count(2) + int(N.count(1)/2)) % 3

        if two_cnt > one_cnt :
            cnt = two_cnt - one_cnt
        else:
            cnt = one_cnt - two_cnt
        
        ans_2 = cnt % 3

        if ans_1 < ans_2 :
            print(ans_1)
        else:
            print(ans_2)


 

