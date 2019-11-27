N = int(input())
words = list(input())

for i in range(len(words)):
    print( chr( (ord(words[i])-ord('A') + N) % 26 + ord('A')) ,end="")
