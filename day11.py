with open('day11.txt') as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip().replace(',','').split(' '))
    
#print(input)

class Monkey:
    def __init__(self, name, items= [], opType = '*', opNum = 1, 
                 testNum = 1 , trueMonkey = 0, falseMonkey = 0):
        self.name = name
        self.items = items
        self.opType = opType
        self.opNum = opNum
        self.testNum = testNum
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        
i = 0
monkeys = []
while i < len(input):
    current = Monkey(name = int(input[i][1][0]), items= [], opType = '*', opNum = 1, 
                 testNum = 1 , trueMonkey = 0, falseMonkey = 0)
                     
    i += 1
    for j in range(2, len(input[i])):
        current.items.append(int(input[i][j]))
        
    i += 1
    if input[i][-1] == 'old':
        current.opType = '**'
        current.opNum = 2
    else:
        current.opType = input[i][-2]
        current.opNum = int(input[i][-1])
        
    i += 1
    current.testNum = int(input[i][-1])
    
    i += 1
    current.trueMonkey = int(input[i][-1])
    
    i += 1
    current.falseMonkey = int(input[i][-1])
    
    monkeys.append(current)
    i += 2
    
#print(monkeys)
monkeyCount = [0 for _ in range(len(monkeys))]
mods = [monkey.testNum for monkey in monkeys]
#print(mods)

for monkey in monkeys:
    for _ in range(len(monkey.items)):
        item = monkey.items.pop(0)
        itemLst = [item % mod for mod in mods]
        monkey.items.append(itemLst)
    #print(monkey.items)

for _ in range(10000):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        monkeyCount[i] += len(monkey.items)
        for _ in range(len(monkey.items)):
            
            current = monkey.items.pop(0)
            
            if monkey.opType == '*':
                for j in range(len(current)):
                    current[j] = (current[j] * monkey.opNum) % mods[j]
            elif monkey.opType == '+':
                for j in range(len(current)):
                    current[j] = (current[j] + monkey.opNum) % mods[j]
            else:
                for j in range(len(current)):
                    current[j] = (current[j]**2) % mods[j]
            #current = int(current/3)
            
            if current[i] == 0:
                nextMonkey = monkey.trueMonkey
            else:
                nextMonkey = monkey.falseMonkey
            
            monkeys[nextMonkey].items.append(current)
    
            
print(monkeyCount)
monkeyCount.sort()
print(monkeyCount[-1] * monkeyCount[-2])
            
            