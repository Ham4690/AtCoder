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

for i in range(2**N):
    print(i)
    speaker = []
    p_list = [0] * N
    for j in range(N):
        if ((i>>j)&1) == 1:
            speaker.append(j)
            p_list[j] = 1

    continue_flag = True
    for s in speaker:
        if continue_flag:
            if s in people.keys():
                A = people[s]
            else:
                continue
            for a in A:
                print(f'a:{a}')
                print(f'p_list[a[0]-1]:{p_list[a[0]-1]}')
                if p_list[a[0]-1] == a[1]:
                     p_list[a[0]-1] = a[1]
                else:
                    continue_flag = False
                    break
        else:
            break
    if continue_flag:
        temp_ans = len(speaker)
        ans = max(temp_ans, ans)

print(ans)
