import re
import numpy as np
import math

inputs = []

with open('./18/input.txt', 'r') as input:
    x, y = 0, 0
    p = 2
    for line in input:
      inputs.append((x, y))
      hex = re.findall(r'\(#(.{6})\)', line)[0]
      dir = hex[-1]
      print(hex)
      if dir == '0':
        x += int(hex[:-1], 16)
      if dir == '2':
        x -= int(hex[:-1], 16)
      if dir == '1':
        y += int(hex[:-1], 16) 
      if dir == '3':
        y -= int(hex[:-1], 16)

      p += int(hex[:-1], 16)

total = 0
for i in range(len(inputs)):
  total += (inputs[i][0] - inputs[i+1 if i+1 != len(inputs) else 0][0]) * (inputs[i+1 if i+1 < len(inputs) else 0][1] + inputs[i][1])

total += p


print(total // 2)
