import sys
from functools import cache
sys.setrecursionlimit(1000000)
import matplotlib.pyplot as plt

map = []

max_found = 0

f_counter = 0
with open('./23/input.txt') as input:
  for li, line in enumerate(input):
    map.append(line[:-1])
    f_counter += line.count('#')

print((len(map) * len(map[0])) - f_counter)

end = (22, 21)
end = (140, 139)
nodes = [(0, 1)]
paths = []

def moves(prev, from_node, count):
  x, y = prev[-1]

  if x == end[0] and y == end[1]:
    nodes.append((x, y))
    paths.append(((from_node, (x, y)), count))
    return

  count_choice = 0
  
  if map[x+1][y] != '#' and (x+1, y) not in prev:
    count_choice += 1

  if map[x-1][y] != '#' and (x-1, y) not in prev:
    count_choice += 1

  if map[x][y+1] != '#' and (x, y+1) not in prev:
    count_choice += 1

  if map[x][y-1] != '#' and (x, y-1) not in prev:
    count_choice += 1

  if count_choice > 1:
    if (x, y) in nodes:
      paths.append(((from_node, (x, y)), count))
      return
    nodes.append((x, y))
    paths.append(((from_node, (x, y)), count))
    count = 0
    from_node = (x, y)
    # print(f"New node {x, y}")


  if map[x+1][y] != '#' and (x+1, y) not in prev:
    moves(prev + [(x+1, y)], from_node, count+1)

  if map[x-1][y] != '#' and (x-1, y) not in prev:
    moves(prev + [(x-1, y)], from_node, count+1)

  if map[x][y+1] != '#' and (x, y+1) not in prev:
    moves(prev + [(x, y+1)], from_node, count+1)

  if map[x][y-1] != '#' and (x, y-1) not in prev:
    moves(prev + [(x, y-1)], from_node, count+1)
  
moves([(0, 1), (1, 1)], (0, 1), 1)

plt.scatter([x[0] for x in nodes], [x[1] for x in nodes])
for p in paths:
  plt.plot([p[0][0][0], p[0][1][0]], [p[0][0][1], p[0][1][1]])
plt.show()

def longest(went, to, traveled=0):
  if went[-1] == to:
    return traveled
  
  max_t = 0

  for path in paths:
    if went[-1] in path[0]:
      
      for dest in path[0]:
        if dest != went[-1] and dest not in went:
          r = longest(went + [dest], to, traveled + path[1])
          max_t = max(max_t, r)

  return max_t

print(longest([nodes[0]], end))
