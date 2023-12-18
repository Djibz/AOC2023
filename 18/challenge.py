import re
import numpy as np
import math

inputs = []

with open('./18/example.txt', 'r') as input:
    rightmost = 0
    bottommost = 0
    leftmost = 0
    topmost = 0
    for line in input:
      (dir, l) = re.findall(r'^(R|U|L|D)\s+(\d+)\s+.*$', line)[0]
      if dir == 'R':
        rightmost += int(l)
      if dir == 'L':
        leftmost += int(l)
      if dir == 'D':
        bottommost += int(l)
      if dir == 'U':
        topmost += int(l)

      inputs.append((dir, int(l)))
    
    print(rightmost, bottommost)

map = np.full((bottommost+2, rightmost+2), 0)

x, y = 0, 0
for input in inputs:
  if input[0] == 'R':
    for i in range(y, y+input[1]+1):
      map[x, i] = 1
    y += input[1]

  if input[0] == 'L':
    for i in range(y-input[1], y):
      map[x, i] = 1
    y -= input[1]

  if input[0] == 'D':
    for i in range(x, x+input[1]+1):
      map[i, y] = 1
    x += input[1]

  if input[0] == 'U':
    for i in range(x-input[1], x):
      map[i, y] = 1
    x -= input[1]

print(map)

for i in range(map.shape[0]):
  inside = False
  for j in range(map.shape[1]):
    if map[i, j] == 1:
      inside = not inside
    if map[i, j] == 0 and inside:
      map[i, j] = 1 

print()
print(map)

def expand(x, y):
  if x < 0 or y < 0 or x >= map.shape[0] or x >= map.shape[1]:
    return

  if map[x, y] != 1:
    map[x, y] = 0