import sys
from functools import cache
sys.setrecursionlimit(1000000)

map = []

max_found = 0

f_counter = 0
with open('./23/input.txt') as input:
  for li, line in enumerate(input):
    map.append(line[:-1])
    f_counter += line.count('#')

print((len(map) * len(map[0])) - f_counter)

def moves(prev):
  results = []

  x, y = prev[-1]

  if x == 123 and y == 131:
    global max_found
    if len(prev) > max_found:
      max_found = len(prev)
      print(max_found)
    return [len(prev)]
  
  if map[x+1][y] != '#' and (x+1, y) not in prev:
    results += moves(prev + [(x+1, y)])

  if map[x-1][y] != '#' and (x-1, y) not in prev:
    results += moves(prev + [(x-1, y)])

  if map[x][y+1] != '#' and (x, y+1) not in prev:
    results += moves(prev + [(x, y+1)])

  if map[x][y-1] != '#' and (x, y-1) not in prev:
    results += moves(prev + [(x, y-1)])

  return results
  
lens = moves([(0, 1), (1, 1)])
print(max(lens) - 1)