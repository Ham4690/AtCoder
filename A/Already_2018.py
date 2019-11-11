y,m,d = input().split("/")
y_list = list(y)
y_list[len(y)-1] = '8'
y = "".join(y_list)
print(y + "/"+m+"/"+d)