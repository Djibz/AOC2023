map = []

pos = set()

with open('./21/example.txt') as input:
  for li, line in enumerate(input):
    if 'S' in line:
      pos.add((li, line.index('S')))
      map.append(line[:-1].replace('S', '.'))
      continue
    map.append(line[:-1])

def available(x, y):
  return map[x % len(map)][y % len(map[0])] == '.'

def next_places(x, y):
  possibles = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
  n_pos = set()
  for p in possibles:
    if available(p[0], p[1]):
      n_pos.add(p)

  return n_pos

for c in range(5000):
  # if c % 100 == 0:
  #   print(c)
  #   print(len(pos))
  new_pos = set()
  for p in pos:
    for r in next_places(p[0], p[1]):
      new_pos.add(r)

  pos = new_pos

print(len(new_pos))
