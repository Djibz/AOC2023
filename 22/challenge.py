bricks = []

with open('./22/example.txt', 'r') as input:
  for line in input:
    b, e = line[:-1].split('~')
    bricks.append(([int(x) for x in b.split(',')], [int(x) for x in e.split(',')]))

def collide(a, b):
  for xa in range(a[0][0], a[0][0] - a[0][0] + 1):
    for ya in range(a[0][1], a[1][1] - a[0][1] + 1):
      for za in range(a[0][2], a[1][2] - a[0][2] + 1):
        for xb in range(b[0][0], b[0][0] - b[0][0] + 1):
          for yb in range(b[0][1], b[1][1] - b[0][1] + 1):
            for zb in range(b[0][2], b[1][2] - b[0][2] + 1):
              if xa == xb and ya == yb and za == zb:
                return True
  return False

def collide_any(brick, bricks):
  for b in bricks:
    if collide(brick, b):
      return True
  return False
  
for b in bricks:
  assert collide_any(b, bricks) == False

def fall_everything(bricks):
  changes = False
  while True:
    for b in bricks:
      if b[0][2] == 0:
        break
      bricks.remove(b)
      new_brick = ((b[0][0], b[0][1], b[0][2] - 1), (b[1][0], b[1][1], b[1][2] - 1))
      if collide_any(new_brick, bricks):
        bricks.append(b)
        break
      

  
