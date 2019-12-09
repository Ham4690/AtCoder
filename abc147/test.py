from collections import Counter
l=['a','b','b','c','b','a','c','c','b','c','b','a']
s=Counter(l)
print(s)
c = sorted(list(s.values()))
c_test = print(sorted(s.values()))
print(c)