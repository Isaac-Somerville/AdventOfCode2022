def makeInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    input = []
    for x in lines:
        y = x.strip()
        line = []
        for char in y:
            line.append(char)
        input.append(line)

    return input

input = makeInput('day25test3.txt')

def snafuToInt(line):
    pow = 0
    total = 0
    for char in line:
        if char == '-':
            total += 5**pow * (-1)
        elif char == '=':
            total += 5**pow * (-2)
        else:
            total += 5**pow * int(char)
        pow += 1
    return total

# total = 0
# for line in input:
#     newTotal = snafuToInt(line[::-1])
#     print(newTotal)
#     total += newTotal

# print(total)
# 31242554356360

def intToSnafu(int):
    pow = 0
    mult = 1
    prod = mult * (5**pow)
    while prod < int:
        if mult == 1:
            mult = 2
        else:
            pow += 1
            mult = 1
        prod = mult * (5**pow)
    
    if mult == 2:
        prod = sum([5**pow] + [2*(5**i) for i in range(pow)])
        if prod >= int:
            mult = 1
        topPow = pow
    
    elif mult == 1:
        prod = sum([2*(5**i) for i in range(pow)])
        if prod < int:
            topPow = pow
        else:
            mult = 2
            topPow = pow-1
    
    # print(mult)
    # print(topPow)
        
    snafuList = [0 for _ in range(topPow)] + [mult]
    coeffs = [-2,-1,0,1,2]
    for pow in range(topPow-1,-1,-1):
        # print(pow)
        prod = sum([snafuList[i] * (5**i) for i in range(topPow+1)])
        # print(prod)
        choices = [prod + (coeff * 5**pow) for coeff in coeffs]
        # print(choices)
        diffs = [abs(int - choice) for choice in choices]
        # print(diffs)
        minDiff = min(diffs)
        # print(minDiff)
        minDiffIdx = diffs.index(minDiff)
        # print(minDiffIdx)
        snafuList[pow] = coeffs[minDiffIdx]
        # print(snafuList)
    
    snafuList.reverse()
    # print(snafuList)
    res = ''
    for char in snafuList:
        if char == -2:
            res += '='
        elif char == -1:
            res += '-'
        else:
            res += str(char)
    
    return res
            

print(intToSnafu(31242554356360))

    
    
    

            
    # if mult == 2:
    #     if (prod - int) < (int - 5**(pow)):
    #         snafuLst = ['2']
    #     else:
    #         mult = 1
    #         snafuLst = ['1']
    #     topPow = pow
    # else:
    #     if (prod - int) < (int - (2 * (5**(pow-1)))):
    #         topPow = pow
    #         snafuLst = ['1']
    #     else:
    #         topPow = pow-1
    #         mult = 2
    #         snafuLst = ['2']

    # currentSum = mult * 5**topPow
    # pows = [topPow - i for i in range(1,topPow+1)]
    # mults = [2,1,0,-1,-2]
    # for pow in pows:
    #     nextSums = [currentSum + mult*(5**pow) for mult in mults]
    #     diffs = [abs(int-nextSum) for nextSum in nextSums]