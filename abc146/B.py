
N = int(input())
words = list(input())

for i in range(len(words)):
    check_word  = ord(words[i]) + N 
    if(check_word > ord('Z')):
        print(chr(ord('A') + (check_word - ord('Z'))-1),end="")
    else:
        print(chr(check_word),end="")
print()
