import bisect

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) //2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1

    return None


N, M = map(int, input().split())

ac = 0
wa = 0

ac_list = []

for i in range(M):
    p, S = input().split()
    q_num = int(p) 
    if  type(binary_search(ac_list, q_num)) is int :
        continue
    else:
        if  S == 'AC':
            ac += 1
            x = int(p) 
            insert_index = bisect.bisect_left(ac_list,x)
            ac_list.insert(insert_index,x)
        else:
            wa += 1

print(str(ac) + " " + str(wa))

