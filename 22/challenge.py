bricks = []

with open('./22/example.txt', 'r') as input:
  for line in input:
    b, e = line[:-1].split('~')
    bricks.append(([int(x) for x in b.split(',')], [int(x) for x in e.split(',')]))

print(bricks)

def share_plan(a, b):
  for i in range(len(a[0])):
    if a[0][i] == a[1][i] == b[0][i] == b[1][i]:
      return i
  return -1

def collide(a, b) -> bool:
  sp = share_plan(a, b)
  if sp == -1:
    return False
  
  if sp == 0:
    pa = (a[1], a[2])
    pb = (b[1], b[2])

  if sp == 1:
    pa = (a[0], a[2])
    pb = (b[0], b[2])

  if sp == 2:
    pa = (a[0], a[1])
    pb = (b[0], b[1])

  if pa[0] != pa[1] and pb[0] != pb[1]:
    if pa[1] != pb[1]:
      return False
    return
  
  return True


def collide_any(brick):
  for b in bricks:
    if collide(brick, b):
      return True
  return False
  
for b in bricks:
  assert collide_any(b) == False
  
