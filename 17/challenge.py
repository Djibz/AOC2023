import numpy as np

lines = []
with open('./17/example.txt', 'r') as input:
    for line in input:
        lines.append([int (x) for x in line[:-1]])

heat_map = np.array([list(x) for x in lines])
print(heat_map.shape)

def h(x, y):
    return x - heat_map.shape[0] + y - heat_map.shape[1]

solutions = []

def run(x, y, ran, heat = 0):
    if x < 0 or y < 0 or x >= heat_map.shape[0] or y >= heat_map.shape[1]:
        return

    n_ran = ran.copy()
    n_ran.append((x, y))
    h = heat_map[x, y]

    if x == heat_map.shape[0] - 1 and y == heat_map.shape[1] - 1:
        solutions.append()
        return

    if len(ran) == 0:
        run(x, y+1, n_ran, heat + h)
        run(x+1, y, n_ran, heat + h)

    if (n_ran[-1][0] == x):
        run(x, y+1, n_ran, heat + h)
        run(x, y-1, n_ran, heat + h)
        if len(n_ran) >=3:
            if n_ran[-2][0] != x or n_ran[-2][0] != x:
                run(x+1, y, n_ran, heat + h)
