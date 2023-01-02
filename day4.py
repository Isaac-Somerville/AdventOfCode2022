with open('day4.txt') as f:
    lines = f.readlines()
    
input = []
for str in lines:
    temp = str.strip().split(",")
    tempLst = []
    for range in temp:
        ends = range.split("-")
        for x in ends:
            tempLst.append(int(x))
    input.append(tempLst)
    
print(input)
    

count = 0
# input = [['2','4','6','8'],
# [2,3,4,5],
# [5,7,7,9],
# [2,8,3,7],
# [6,6,4,6],
# [2,6,4,8]]
# i = 0
#print(len(input))
# while i < len(input):
#     start1, end1, start2, end2 = input[i]
#     if (start1 <= start2 and end2 <= end1) or (start2 <= start1 and end1 <= end2):
#         count += 1
#     i += 1

# print(count)

for pair in input:
    start1, end1, start2, end2 = pair
    if (start1 <= start2 <= end1) or (start1 <= end2 <= end1) or (start2 <= start1 <= end2) or (start2 <= end1 <= end2):
        count += 1

print(count)