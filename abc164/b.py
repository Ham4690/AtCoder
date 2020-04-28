hp, atk, e_hp, e_atk = map(int, input().split())

count = 1
while hp > 0 and e_hp > 0 :
  if count % 2 == 1:
    e_hp -= atk 
  else:
    hp -= e_atk
  count += 1

if hp > 0 :
  print('Yes')
else:
  print('No')