from functools import cache
map = []

pos = set()

with open('./21/example.txt') as input:
  for li, line in enumerate(input):
    if 'S' in line:
      pos.add((li, line.index('S')))
      map.append(line[:-1].replace('S', '.'))
      continue
    map.append(line[:-1])

@cache
def available(x, y):
  return map[x][y] == '.'

@cache
def next_places(x, y):
  possibles = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
  n_pos = set()
  for p in possibles:
    if available(p[0] % len(map), p[1] % len(map[0])):
      n_pos.add(p)

  return n_pos

@cache
def pre_next_places(x, y):
  deltax = (x // len(map)) * len(map)
  deltay = (y // len(map[0])) * len(map[0])
  return [(s[0] + deltax, s[1] + deltay) for s in next_places(x - deltax, y - deltay)]

for c in range(5000):
  if c % 100 == 0:
    print(c)
  #print(f"len : {len(pos)}")
  new_pos = set()
  for p in pos:
    for r in pre_next_places(p[0], p[1]):
      new_pos.add(r)

  #print(f"gro : { c / len(pos)}")
  pos = new_pos

print(len(new_pos))
