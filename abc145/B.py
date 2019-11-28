N = int(input())
words = list(input())
if(len(words) % 2 == 1 ):
    print("No")
else:
    center = int(len(words) / 2)
    words_f = words[:center]
    words_b = words[center:]
    if(words_f == words_b):
        print("Yes")
    else:
        print("No")


    