import re

LARGING = 999999

matrix = []
with open('./11/input.txt', 'r') as input:
  void_columns = set()
  void_lines = []
  for k, line in enumerate(input):
    if k == 0:
      void_columns = set([i for i in range(len(line)-1)])
    void_columns = void_columns.intersection(set([m.start() for m in re.finditer(r'\.', line)]))
    if len(re.findall(r'#', line)) == 0:
      void_lines.append(k)
    matrix.append(list(line[:-1]))

  print(void_columns)
  print(void_lines)
  cl = list(void_columns)
  cl.sort()

  #for col in reversed(cl):
  #  for i in reversed(range(len(matrix))):
  #    matrix[i].insert(col, '.')

  void_lines.sort()
  #for line in reversed(void_lines):
  #  matrix.insert(line, ['.' for _ in range(len(matrix[0]))])

  galaxies = []
  for l in range(len(matrix)):
    for c in range(len(matrix[0])):
      if matrix[l][c] == '#':
        galaxies.append((l, c))


  total = 0
  for g in galaxies:
    for g2 in galaxies:
      if g[0] == g2[0] and g[1] == g2[1]:
        continue

      for i in void_lines:
        if (i > g[0] and i < g2[0]) or (i < g[0] and i > g2[0]):
          total += LARGING

      for i in cl:
        if (i > g[1] and i < g2[1]) or (i < g[1] and i > g2[1]):
          total += LARGING

      total += abs(g[0] - g2[0]) + abs(g[1] - g2[1])

  print(total / 2)