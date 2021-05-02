N, D, H = map(int, input().split())

d_list = []
h_list = []
tilt_list = []
intercept_list = []
for i in range(N):
    d, h = map(int, input().split())
    d_list.append(d)
    h_list.append(h)
    tilt = (H-h)/(D-d)
    tilt_list.append(tilt)
    intercept = H-tilt * D   
    if intercept < 0 :
        intercept_list.append(0.0)
    else:
        intercept_list.append(intercept)

print(max(intercept_list))
    

