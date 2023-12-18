import sys
sys.setrecursionlimit(1000000)


lines = []
with open('./17/input.txt', 'r') as input:
    for line in input:
        lines.append([int (x) for x in line[:-1]])

heat_map = [list(x) for x in lines]
shape_m = (len(heat_map), len(heat_map[0]))
best = [[-1 for _ in range(shape_m[1])] for _ in range(shape_m[0])]
print(shape_m)

def h(x, y):
    return (x - shape_m[0] + y - shape_m[1]) * min(heat_map)

solutions = []

def run(x, y, heat = 0, col=0, row=0):
    print(0)
    if x < 0 or y < 0 or x >= shape_m[0] or y >= shape_m[1]:
        return

    h = heat_map[x][y]

    print(1)

    if best[x][y] == -1 or best[x][y] > h + heat:
        best[x][y] = h + heat
    else:
        return 
    
    print(2)

    if x == shape_m[0] - 1 and y == shape_m[1] - 1:
        return
    
    print(3)

    if row == 0 and col == 0:
        run(x, y+1, heat + h, col=0, row=1)
        run(x+1, y, heat + h, col=1, row=0)
        return
    
    print(4)

    if (row == 0):
        run(x, y+1, heat + h, col=0, row=1)
        run(x, y-1, heat + h, col=0, row=1)
        if col < 4:
            run(x+1, y, heat + h, col=col+1, row=0)

    print(5)

    if (col == 0):
        run(x-1, y, heat + h, col=1, row=0)
        run(x+1, y, heat + h, col=1, row=0)
        if row < 4:
            run(x, y+1, heat + h, col=0, row=row+1)

run(0, 0)

#print(best)