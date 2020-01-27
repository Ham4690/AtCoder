import bisect
a=[]
x=4

insert_index = bisect.bisect_left(a,x)


a.insert(insert_index,x)

print(a)