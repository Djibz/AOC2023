map = []

pos = set()

with open('./21/input.txt') as input:
  for li, line in enumerate(input):
    if 'S' in line:
      pos.add((li, line.index('S')))
      map.append(line[:-1].replace('S', '.'))
      continue
    map.append(line[:-1])

print(map)
print(pos)

def available(x, y):
  return x >= 0 and y >= 0 and x < len(map) and y < len(map[0]) and map[x][y] == '.'

def next_places(x, y):
  possibles = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
  n_pos = set()
  for p in possibles:
    if available(p[0], p[1]):
      n_pos.add(p)

  return n_pos

for _ in range(64):
  new_pos = set()
  for p in pos:
    for r in next_places(p[0], p[1]):
      new_pos.add(r)

  pos = new_pos

print(len(new_pos))