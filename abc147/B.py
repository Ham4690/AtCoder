word = list(input())
word_t = word[::-1]
count = 0
wordhalf = int(len(word)/2)
for i in range(wordhalf):
    if word[i] != word[-(i+1)]:
        count += 1
print(count)
