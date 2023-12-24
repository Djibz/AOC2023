import numpy as np
import sys
sys.setrecursionlimit(1000000)

map = []

max_found = 0

with open('./23/input.txt') as input:
  for li, line in enumerate(input):
    map.append(line[:-1])

end = (140, 139)

def resolvable(trav, x, y):
  if x == end[0] and y == end[1]:
    return True
  if map[x][y] == '#':
    return False
  if (x, y) in trav:
    return False

  trav.append((x, y))
  
  if resolvable(trav, x+1, y): return True
  if resolvable(trav, x-1, y): return True
  if resolvable(trav, x, y+1): return True
  if resolvable(trav, x, y-1): return True

  return False

def moves(prev):
  results = []

  x, y = prev[-1]

  if False and len(prev) % 50 == 0:
    if not resolvable(prev.copy()[:-1], x, y):
      return []

  if x == end[0] and y == end[1]:
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