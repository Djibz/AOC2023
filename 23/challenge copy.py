import numpy as np
import sys
sys.setrecursionlimit(1000000)

map = []

max_found = 0

with open('./23/input.txt') as input:
  for li, line in enumerate(input):
    map.append(line[:-1])

def moves(prev):
  results = []

  x, y = prev[-1]

  if x == len(map) - 1:
    global max_found
    if len(prev) > max_found:
      max_found = len(prev)
      print(max_found)
    return [len(prev)]
  
  if map[x+1][y] in '.<>^v' and (x+1, y) not in prev:
    results += moves(prev + [(x+1, y)])

  if map[x-1][y] in '.<>^v' and (x-1, y) not in prev:
    results += moves(prev + [(x-1, y)])

  if map[x][y+1] in '.<>^v' and (x, y+1) not in prev:
    results += moves(prev + [(x, y+1)])

  if map[x][y-1] in '.<>^v' and (x, y-1) not in prev:
    results += moves(prev + [(x, y-1)])

  return results
  
lens = moves([(0, 1), (1, 1)])
print(max(lens) - 1)