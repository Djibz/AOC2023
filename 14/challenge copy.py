import numpy as np
import re
from functools import cache
import threading
import concurrent.futures

lines = []

with open('./14/input.txt', 'r') as input:
    for line in input:
        lines.append(line[:-1])

nparr = np.array([list(x) for x in lines])
transpose = [''.join(x) for x in nparr.transpose().tolist()]

@cache
def slide_row(row):
    parts = row.split('#')
    new_parts = []
    for part in parts:
        nb_r = len(re.findall(r'O', part))
        new_parts.append(('O' * nb_r) + ('.' * (len(part) - nb_r)))
    return '#'.join(new_parts)


def slide_west(plate):
    new_cols = []
    for col in plate:
        new_cols.append(slide_row(col))
    return new_cols

def rocks_load(plate):
    total = 0
    for col in plate:
        for i, c in enumerate(list(reversed(col))):
                if c == "O": total += i + 1
    return total

def rotate_clock(plate):
    nparr = np.array([list(x) for x in plate])
    return [''.join(list(reversed(x))) for x in (nparr.transpose().tolist())]

def rotate_anti(plate):
    nparr = np.array([list(reversed(x)) for x in plate])
    return [''.join(x) for x in (nparr.transpose().tolist())]

def spin_cycle(plate):
    return rotate_clock(slide_west(rotate_clock(slide_west(rotate_clock(slide_west(rotate_clock(slide_west(plate))))))))

state = slide_west(rotate_anti(lines))
total = rocks_load(state)

print(f"Part 1 : {total}")

print()

def hash_plate(plate):
    return ''.join(plate)

visited = dict()

state = lines
last = 0
for i in range(999999999):
    state = rotate_clock(spin_cycle(rotate_anti(state)))
    if hash_plate(state) in visited:
        cycle = i - visited[hash_plate(state)]
        last = (999999999 - i) % cycle
        break
    visited[hash_plate(state)] = i
print(last)

for i in range(last):
    state = rotate_clock(spin_cycle(rotate_anti(state)))

for i in state:
    print(i)

print(rocks_load(rotate_anti(state)))