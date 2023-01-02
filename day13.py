with open('day13.txt') as f:
    lines = f.readlines()
    
def makeList(s):
    j = 0 
    lst = []
    temp = ''
    while j < len(s) and s[j] != ']':
        if s[j] == ',':
            if temp:
                lst.append(int(temp))
                temp = ''
            j += 1
        elif s[j] == '[':
            k, newLst = makeList(s[j+1:])
            lst.append(newLst)
            j += k
        else:
            if temp:
                temp += s[j]
            else:
                temp = s[j]
            j += 1
    if temp:
        lst.append(int(temp))
    return j+2, lst
    
temp = []
for line in lines:
    j , lst = makeList(line.strip()[1:])
    temp.append(lst)

input = []
for i in range(len(temp)):
    if (i + 1) % 3 != 0:
        input.append(temp[i])

input.append([[2]])
input.append([[6]])
for lst in input:
    print(lst)

def isInOrder(l,r):
    j = 0
    while j < len(l) and j < len(r):
        if type(l[j]) == int:
            if type(r[j]) == int:
                if l[j] < r[j]:
                    return True
                elif r[j] < l[j]:
                    return False

            else: # r[j] is a list, compare with [l[j]]
                temp = isInOrder([l[j]],r[j])
                if temp == True:
                    return True
                elif temp == False:
                    return False

        elif type(l[j]) == list:
            if type(r[j]) == list:
                temp = isInOrder(l[j],r[j])
                if temp == True:
                    return True
                elif temp == False:
                    return False
            
            else: # l[j] is a list, compare with [r[j]]
                temp = isInOrder(l[j], [r[j]])
                if temp == True:
                    return True
                elif temp == False:
                    return False
        j += 1
    
    if j != len(l): # len(r) < len(l)
        return False

    if j != len(r): #len(l) < len(r)
        return True

    return None


# idx = 1
# i = 0
# idxList = []
# while i < len(input):
#     l = input[i]
#     r = input[i+1]
#     print(l)
#     print(r)
#     if isInOrder(l,r) == True:
#         idxList.append(idx)
#     i += 2
#     idx += 1

# print(idxList)
# print(sum(idxList))

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if isInOrder(L[i],R[j]) == True:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

mergeSort(input)
print(input)
a = input.index([[2]]) + 1
b = input.index([[6]]) + 1
print(a,b,a*b)