import re

with open('./2/input.txt', 'r') as input:

  print("Part 1")
  total = 0
  for line in input:
    ID = re.findall
    first = re.findall(r'^[^0-9]*?([0-9])', line)[0]
    last = re.findall(r'([0-9])[^0-9]*?$', line)[0]
    total += int(first+last)