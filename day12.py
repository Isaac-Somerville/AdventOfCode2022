with open('day12.txt') as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())
 
    
grid = []
starts = []
for i in range(len(input)):
    row = []
    for j in range(len(input[i])):
        if input[i][j].islower() and input[i][j] != 'a':
            row.append(ord(input[i][j])-96)
        elif input[i][j] == 'S' or input[i][j] == 'a':
            row.append(1)
            starts.append((i,j))
        elif input[i][j] == 'E':
            row.append(26)
            end = (i,j)
    grid.append(row)

drxns = [(-1,0), (1,0), (0,1), (0,-1)]
n = len(grid)
m = len(grid[0])
stepLst = []

for start in starts:
    visited = {start}
    queue = [start]
    steps = 0
    while queue:
        for _ in range(len(queue)):
            x, y  = queue.pop(0)
            for vMove, hMove in drxns:
                if (x+vMove,y+hMove) not in visited and 0<= x + vMove < n and 0 <= y + hMove < m:
                    if grid[x+vMove][y+hMove] <= grid[x][y] + 1:
                        queue.append((x+vMove,y+hMove))
                        visited.add((x+vMove,y+hMove))
        steps += 1
        if end in visited:
            stepLst.append(steps)
            break
        
print(min(stepLst))