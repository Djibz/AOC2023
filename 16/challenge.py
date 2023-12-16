import sys

matrix = []
power_m = []
sys.setrecursionlimit(1000000)


went = []
def run_light(dir, x, y):
  if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix):
    return
  
  if (dir, x, y) in went:
    return

  went.append((dir, x, y))
  power_m[y][x] = 1

  if matrix[y][x] == '.':
    if dir == 'right':
      run_light(dir, x+1, y)
    elif dir == 'left':
      run_light(dir, x-1, y)
    elif dir == 'top':
      run_light(dir, x, y-1)
    elif dir == 'bottom':
      run_light(dir, x, y+1)

  elif matrix[y][x] == '|':
    if dir in ['right', 'left']:
      run_light('top', x, y-1)
      run_light('bottom', x, y+1)
    elif dir == 'top':
      run_light(dir, x, y-1)
    elif dir == 'bottom':
      run_light(dir, x, y+1)

  elif matrix[y][x] == '-':
    if dir in ['top', 'bottom']:
      run_light('right', x+1, y)
      run_light('left', x-1, y)
    elif dir == 'left':
      run_light(dir, x-1, y)
    elif dir == 'right':
      run_light(dir, x+1, y)

  elif matrix[y][x] == '/':
    if dir == 'right':
      run_light('top', x, y-1)
    elif dir == 'left':
      run_light('bottom', x, y+1)
    elif dir == 'top':
      run_light('right', x+1, y)
    elif dir == 'bottom':
      run_light('left', x-1, y)

  elif matrix[y][x] == '\\':
    if dir == 'right':
      run_light('bottom', x, y+1)
    elif dir == 'left':
      run_light('top', x, y-1)
    elif dir == 'top':
      run_light('left', x-1, y)
    elif dir == 'bottom':
      run_light('right', x+1, y)

with open('./16/input.txt', 'r') as input:
  for line in input:
    matrix.append(line[:-1])
    power_m.append([0 for _ in range(len(line)-1)])

run_light('right', 0, 0)

def count():
  total = 0
  for l in power_m:
    total += sum(l)
  return total

print(f"Part 1 : {count()}")

c=0
init_power = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
founds = []
for y in range(len(matrix)):
  went = []
  power_m = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
  run_light('right', 0, y)
  founds.append(count())

  went = []
  power_m = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
  run_light('left', len(matrix)-1, y)
  founds.append(count())
  print(f"{50*c/len(matrix)}%")
  c+= 1

c=0
for x in range(len(matrix[0])):
  went = []
  power_m = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
  run_light('bottom', x, 0)
  founds.append(count())

  went = []
  power_m = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
  run_light('top', x, len(matrix[0])-1)
  founds.append(count())
  print(f"{50 + (50*c/len(matrix))}%")
  c+= 1

print(f"Part 2 : {max(founds)}")