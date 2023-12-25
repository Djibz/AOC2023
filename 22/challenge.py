bricks = []
on = dict()
below = dict()

with open('./22/example.txt', 'r') as input:
  for k, line in enumerate(input):
    b, e = line[:-1].split('~')
    bricks.append(([int(x) for x in b.split(',')], [int(x) for x in e.split(',')], k))
    on[k] = []
    below[k] = []

def collide(a, b):
  for xa in range(a[0][0], a[1][0]+1):
    for ya in range(a[0][1], a[1][1]+1):
      for za in range(a[0][2], a[1][2]+1):
        for xb in range(b[0][0], b[1][0]+1):
          for yb in range(b[0][1], b[1][1]+1):
            for zb in range(b[0][2], b[1][2]+1):
              if xa == xb and ya == yb and za == zb:
                return True
  return False

def collide_any(brick, bricks):
  for b in bricks:
    if collide(brick, b):
      return True
  return False
  
def collide_with(brick, bricks):
  c_with = []
  for b in bricks:
    if collide(brick, b):
      c_with.append(b[2])
  return c_with

for i in range(len(bricks)):
  assert collide_any(bricks[i], bricks[:i] + bricks[i+1:]) == False

print("Initial stable\n")

def fall_everything(bricks):
  a_change = False
  while True:
    changes = False
    for i in range(len(bricks)):
      if bricks[i][0][2] == 0:
        continue
      in_z = bricks[i][0][2]
      while not collide_any(bricks[i], bricks[:i] + bricks[i+1:]):
        if bricks[i][0][2] < 0:
          break
        bricks[i][0][2] -= 1
        bricks[i][1][2] -= 1
      bricks[i][0][2] += 1
      bricks[i][1][2] += 1
      if in_z != bricks[i][0][2]:
        changes = True
        a_change = True
    if not changes:
      break
  return a_change

def one_falling(bricks):
  for i in range(len(bricks)):
    if bricks[i][0][2] == 0:
      continue
    new_brick = ([bricks[i][0][0], bricks[i][0][1], bricks[i][0][2] - 1], [bricks[i][1][0], bricks[i][1][1], bricks[i][1][2] - 1])
    if not collide_any(new_brick, bricks[:i] + bricks[i+1:]):
      return True
  return False

bricks.sort(key=lambda x: x[0][2])

while fall_everything(bricks):
  ""


for i in range(len(bricks)):
  assert collide_any(bricks[i], bricks[:i] + bricks[i+1:]) == False

print("Falled stable\n")

print(f"Nb briques : {len(bricks)}")

assert not one_falling(bricks)

for i, b in enumerate(bricks):
  c = collide_with(([b[0][0], b[0][1], b[0][2] - 1], [b[1][0], b[1][1], b[1][2] - 1], -1), bricks[:i] + bricks[i+1:])
  on[b[2]] = c
  for bel in c:
    below[bel].append(b[2])

print("graph done")

critic = set()
for k, v in on.items():
  if len(v) == 1:
    critic.add(v[0])

print("Part 1 : ", end='')
print(len(bricks) - len(critic))

# total = 0
# for i, b in enumerate(bricks):
#   if not one_falling(bricks[:i] + bricks[i+1:]):
#     total += 1

# print(f"Part1 : {total}")


def fall_from(brick, fallen=[]):
  stable = False
  for bel in on[brick]:
    if bel not in fallen:
      stable = True
  if stable: return 0

  fallen.append(brick)

  reperc = 1
  for u in below[brick]:
    reperc += fall_from(u, fallen)

  return reperc

total = 0
for cri in critic:
  total += fall_from(cri)

print("Part 2 : ", end='')
print(total - len(critic))