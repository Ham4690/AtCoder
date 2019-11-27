days = ['SUN','MON','TUE','WED','THU','FRI','SAT']

day = input()
for i in range(len(days)):
    if day == days[i]:
        print(7-i)
