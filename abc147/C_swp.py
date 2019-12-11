N = int(input())
people = {}

for i in range(N):
    A = int(input())
    if A > 0:
        for j in range(A):
            v = list(map(int,input().split()))
            if i in people.keys():
                people[i].append(v)
            else:
                people[i] = [v]

ans = 0
print(f"N:{N}")
print(f"people{people}")
print(f"people.keys():{people.keys()}")

for i in range(2**N):
    speaker = []
    p_list = [0] * N
    for j in range(N):
        if ((i>>j)&1) == 1:
            speaker.append(j)
            p_list[j] = 1

    print(f"speaker:{speaker}") #speakerには正直者のindexが入る
    print(f"p_list:{p_list}") #p_listには正直者の場所に１を入れる

    continue_flag = True
    for s in speaker:
        print(f"s:{s}")
        if continue_flag:
            if s in people.keys():
                # print(A)
                A = people[s] #正直ものだと課程した人物の証言をとりだしてAへ入れている
            else:
                continue

            for a in A: #正直者だと仮定した人物の証言のチェック
                print(f'a:{a}')
                # print(f'p_list[a[0]-1]:{p_list[a[0]-1]}')

                if p_list[a[0]-1] == a[1]:
                     print(f"p_list[a[0]-1]{p_list[a[0]-1]}")
                     p_list[a[0]-1] = a[1]
                else:
                    continue_flag = False
                    print("[false]")
                    print(f"p_list[a[0]-1]:{p_list[a[0]-1]}")
                    print(f"a[1]:{a[1]}")
                    break
        else:
            break
    if continue_flag:
        temp_ans = len(speaker)
        ans = max(temp_ans, ans)
    print(f"----:{i}")

print(ans)
