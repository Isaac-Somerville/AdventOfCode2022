lists = [["_"],
         ["S","T","H","F","W","R"],
         ["S","G","D","Q","W"],
         ["B","T","W"],
         ["D","R","W","T","N","Q","Z","J"],
         ["F","B","H","G","L","V","T","Z"],
         ["L","P","T","C","V","B","S","G"],
         ["Z","B","R","T","W","G","P"],
         ["N","G","M","T","C","J","R"],
         ["L","G","B","W"]
]

with open('day5.txt') as f:
    lines = f.readlines()
    
input = []
for str in lines:
    temp = str.strip().split(" ")
    inst = [int(temp[i]) for i in [1,3,5]]
    input.append(inst)
    
print(input)

# for inst in input:
#     count, source, dest = inst
#     for _ in range(count):
#         lists[dest].append(lists[source].pop())
    
# print(lists)
# res = []
# for lst in lists:
#     res.append(lst[-1])

# res.pop(0)
# print("".join(res))

for inst in input:
    count, source, dest = inst
    n = len(lists[source])
    temp = lists[source][n-count:]
    lists[dest] += temp
    lists[source] = lists[source][:n-count]
    
print(lists)
res = []
for lst in lists:
    res.append(lst[-1])

res.pop(0)
print("".join(res))