import re
import numpy as np
import math

inputs = []

with open('./18/input.txt', 'r') as input:
    x, y = 0, 0
    p = 2
    for line in input:
      inputs.append((x, y))
      (dir, l) = re.findall(r'^(R|U|L|D)\s+(\d+)\s+.*$', line)[0]
      if dir == 'R':
        x += int(l)
      if dir == 'L':
        x -= int(l)
      if dir == 'D':
        y += int(l) 
      if dir == 'U':
        y -= int(l)

      p += int(l)

print(p)

total = 0
for i in range(len(inputs)):
  total += (inputs[i][0] - inputs[i+1 if i+1 != len(inputs) else 0][0]) * (inputs[i+1 if i+1 < len(inputs) else 0][1] + inputs[i][1])

total += p


print(total / 2)
