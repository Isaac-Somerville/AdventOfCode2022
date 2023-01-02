with open('day10.txt') as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip().split(' '))
    
print(input)

# =============================================================================
# cycles = 1
# x = 1
# signals = []
# for line in input:
#     if line[0] == 'noop':
#         if (cycles - 20 ) % 40 == 0:
#             signals.append(cycles * x)
#         cycles += 1
#     else:
#         for _ in range(2):
#             if (cycles - 20 ) % 40 == 0:
#                 signals.append(cycles * x)
#             cycles += 1
#         x += int(line[1])
#         
# print(signals)
# print(sum(signals))
# =============================================================================

image = [['.' for _ in range(40)] for _ in range(6)]
cycles = 0
coords = [cycles//40, cycles % 40 ]
print(coords)
x = 1
pixie = [0,1,2]
for line in input:
    if line[0] == 'noop':
        if coords[1] in pixie:
            image[coords[0]][coords[1]] = '#'
        cycles += 1
        coords = [cycles//40, cycles % 40]
    else:
        for _ in range(2):
            if coords[1] in pixie:
                image[coords[0]][coords[1]] = '#'
            cycles += 1
            coords = [cycles//40, cycles % 40]
        x += int(line[1])
        pixie = [x-1, x, x+1]
        
print(image)