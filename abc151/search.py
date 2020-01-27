my_list = []
# for i in range(100000):
#     my_list.append(i)

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

if (type(binary_search(my_list, 77)) is int):
    print("yes")
else:
    print("no")
print (binary_search(my_list, 77))