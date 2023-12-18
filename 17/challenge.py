import numpy as np
import sys
sys.setrecursionlimit(1000000)


lines = []
with open('./17/example.txt', 'r') as input:
    for line in input:
        lines.append([int (x) for x in line[:-1]])

heat_map = np.array([list(x) for x in lines])
best = np.full(heat_map.shape, -1)
print(heat_map.shape)

def h(x, y):
    return (x - heat_map.shape[0] + y - heat_map.shape[1]) * min(heat_map)

solutions = []

def run(x, y, ran, heat = 0):
    if x < 0 or y < 0 or x >= heat_map.shape[0] or y >= heat_map.shape[1] or (x, y) in ran:
        return

    n_ran = ran.copy()
    n_ran.append((x, y))
    h = heat_map[x, y]
    

    if x == heat_map.shape[0] - 1 and y == heat_map.shape[1] - 1:
        solutions.append((heat + h, n_ran))
        return

    if len(ran) == 0:
        run(x, y+1, n_ran, heat + h)
        run(x+1, y, n_ran, heat + h)

    if (ran[-1][0] == x):
        run(x, y+1, n_ran, heat + h)
        run(x, y-1, n_ran, heat + h)
        if len(n_ran) >=3:
            if ran[-2][0] != x or ran[-3][0] != x:
                run(x+1, y, n_ran, heat + h)

    if (ran[-1][1] == y):
        run(x-1, y, n_ran, heat + h)
        run(x+1, y, n_ran, heat + h)
        if len(n_ran) >=3:
            if ran[-2][1] != y or ran[-3][1] != y:
                run(x, y+1, n_ran, heat + h)

                

run(0, 0, [])

print(min(solutions, key=lambda x: x[0]))