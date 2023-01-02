import sys

sys.setrecursionlimit(2000)

class Node:
    def __init__(self,name,val = None, left = None, right = None, op = None):
        self.name = name
        self.val = val
        self.left = left
        self.right = right
        self.op = op

def makeInput(file):
    with open(file) as f:
        lines = f.readlines()

    treeDict = {}
    for x in lines:
        line = x.strip().split(' ')
        # print(line)
        current = Node(line[0][:4])
        if len(line) > 2:
            current.left = line[1]
            #print(current.left)
            if current.name == 'root':
                current.op = '='
            else:
                current.op = line[2]
                #print(current.op)
            current.right = line[3]
            #print(current.right)
        elif current.name == 'humn':
            current.val = 'x'
        else:
            current.val = line[1]
        treeDict[current.name] = current
        # print(current.name,current.val,current.left,current.op,current.right)
    #print(treeDict)

    for node in treeDict:
        if treeDict[node].left:
            treeDict[node].left = treeDict[treeDict[node].left]
        if treeDict[node].right:
            treeDict[node].right = treeDict[treeDict[node].right]

    return treeDict

file = 'day21.txt'
treeDict = makeInput(file)
root = treeDict['root']

def findRootVal(root):
    # print(root.name)
    # print(root.val)
    if root.val != None:
        return root.val
    
    left = findRootVal(root.left)
    right = findRootVal(root.right)
    if root.op == '+':
        output = '(' + left + '+' + right + ')'
        #print(output)
        return output
    if root.op == '-':
        output = '(' + left + '-' + right + ')'
        #print(output)
        return output
    if root.op == '*':
        output = '(' + left + '*' + right + ')'
        #print(output)
        return output
    if root.op == '/':
        output = '(' + left + '/' + right + ')'
        #print(output)
        return output
    if root.op == '=':
        output = '(' + left + '=' + right + ')'
        #print(output)
        return output

equation = findRootVal(root)
LHS, RHS = equation.split('=')
LHS = LHS[1:] # ((((155298606319083-(10*(((((((((3*((((((((((((((((((10*(((421+((((2*(((((807+(789+((((383+((128+((((((12*(((385+(((57+(((((2*(396+((383+((17*(x-214))+918))/5)))-200)/7)-569)/3))*15)-971))/2)+744))-924)*2)+781)+188)/3))+360))/2)-94)*2)))/2)-470)*3)+96))-423)/3)-480))/6)+40))+416)*2)-871)/3)+364)*2)-636)/2)-486)*2)+973)/3)-383)*2)+967)/3)+603))-539)+440)/7)-556)*3)+587)/4)+591)))+185)/9))
RHS = RHS[:-1] # 3952741911612
ops = {'+','-','*','/'}

def evaluate(equation, ops):
    rIdx = equation.find(')')
    if rIdx == -1:
        if equation.find('x') != -1:
            return '[' + equation + ']'
        print(equation)
        i = 0
        LHS = ''
        while i < len(equation) and equation[i] not in ops:
            LHS += equation[i]
            i += 1
        
        if i == len(equation):
            return LHS
        op = equation[i]
        i += 1
        RHS = ''
        while i < len(equation):
            RHS += equation[i]
            i += 1
        
        if op == '+':
            return str(int(int(LHS)+int(RHS)))
        if op == '-':
            return str(int(int(LHS)-int(RHS)))
        if op == '*':
            return str(int(LHS)*int(RHS))
        if op == '/':
            return str(int(int(LHS)/int(RHS)))
    
    i = rIdx - 1
    while equation[i] != '(':
        i -= 1
    
    output = equation[:i] + evaluate(equation[i+1:rIdx],ops) + equation[rIdx+1:]
    return evaluate(output,ops)
    

LHS = evaluate(LHS,ops)
temp = LHS.replace('[','(')
temp1 = temp.replace(']',')')
print(temp1)