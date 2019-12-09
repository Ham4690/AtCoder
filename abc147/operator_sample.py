from operator import itemgetter
B =[(5,8), (6,10), (7,2),(4,1), (3,11),(9,0)]
print(f'B:{B}')
print(sorted(B, key = itemgetter(0))) #第1変数で昇順ソートしてる
#[(3, 11), (4, 1), (5, 8), (6, 10), (7, 2), (9, 0)]
print(sorted(B, key = itemgetter(0),reverse=True)) #第1変数で降順ソートしてる
#[(9, 0), (7, 2), (6, 10), (5, 8), (4, 1), (3, 11)]
print(sorted(B, key = itemgetter(1))) #第2変数で昇順ソートしてる
#[(9, 0), (4, 1), (7, 2), (5, 8), (6, 10), (3, 11)]
print(sorted(B, key = itemgetter(1),reverse=True)) #第2変数で降順ソートしてる
#[(3, 11), (6, 10), (5, 8), (7, 2), (4, 1), (9, 0)]
