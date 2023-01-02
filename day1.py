with open('day1.txt') as f:
    lines = f.readlines()
    
res = []
for str in lines:
    res.append(str.strip())
    
countList = []
top3 = []
third = 0
count = 0
for cal in res:
    if cal:
        count += int(cal)
    else:
        countList.append(count)
        if len(top3) < 3:
            top3.append(count)
            third = min(top3)
        elif count > third:
            top3.remove(third)
            top3.append(count)
            third = min(top3)
        count = 0

print(countList)
print(top3)
print(sum(top3))