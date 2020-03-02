def isBingo(card):

    con = 1
    for i in range(3):
        con = 1
        for j in range(3):
            con += card[i][j]
        if con == 1:
            return True

    con = 1
    for i in range(3):
        con = 1
        for j in range(3):
            con += card[j][i]
        if con == 1:
            return True

    if(card[1][1] == card[0][0] and card[1][1] == card[2][2]):
        return True
    
    if(card[1][1] == card[0][2] and card[1][1] == card[2][0]):
        return True
    
    return False

bingo_nums = [[0 for i in range(3)] for j in range(3)]

for i in range(3):
    a,b,c = map(int,input().split())
    bingo_nums[i][0] = a
    bingo_nums[i][1] = b
    bingo_nums[i][2] = c


N = int(input())
for i in range(N):
    num = int(input())
    
    for i in range(3):
        for j in range(3):
            if bingo_nums[i][j] == num:
                bingo_nums[i][j] = 0
                break
            
if isBingo(bingo_nums):
    print('Yes')
else:
    print('No')