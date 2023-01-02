class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        #self.prev = prev

def makeInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    lst = []
    prev = None
    for x in lines:
        current = ListNode(int(x.strip()) * 811589153)
        if current.val == 0:
            zero = current
        #current.prev = prev
        if prev:
            prev.next = current
        lst.append(current)
        prev = current

    current.next = lst[0]
    #lst[0].prev = current

    return lst, zero

file = 'day20.txt'

order, zero = makeInput(file)
llst = order.copy()

i = 0
n = len(order)
current = order[0]
# for j in range(n):
#     print(order[j].val)
#     print(current.val)
#     current = current.next
for _ in range(10):
    print(_)
    for i in range(n):
        current = order[i]
        prev = current
        while prev.next != current:
            prev = prev.next
        val = current.val % (n-1)
        #print(val)
        for _ in range(val):
            curNext = current.next
            current.next = curNext.next
            curNext.next = current
            prev.next = curNext
            prev = curNext

current = zero
# temp = zero
# for _ in range(n):
#     print(temp.val)
#     temp = temp.next

totalSum = 0
for i in range(3):
    for j in range(1000):
        current = current.next
    print(i,current.val)
    totalSum += current.val

print("totalSum  = ", totalSum)

        