scores = [
    {'kokugo': 33, 'sansuu': 85},
    {'kokugo': 77, 'sansuu': 23},
    {'kokugo': 55, 'sansuu': 100}
]

scores_sorted = sorted(scores, key=lambda x:x['kokugo'])

print(scores_sorted) 