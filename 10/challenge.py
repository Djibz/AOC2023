import math
import sys
sys.setrecursionlimit(1000000)

matrix = []
m_length = []
m_matrix = []
i_matrix = []

def print_m(m):
  for i in m:
    print(i)

with open('./10/input.txt', 'r') as input:
  start = 0
  for k, line in enumerate(input):
    matrix.append(line[:-1])
    m_length.append([-1 for _ in range(len(line) - 1)])
    m_matrix.append(['.' for _ in range(len(line) - 1)])
    i_matrix.append([0 for _ in range(len(line) - 1)])
    if 'S' in line[:-1]:
      start =  k

def explore(x, y, dist):
  if (m_length[x][y] != -1 and m_length[x][y] < dist):
    return

  m_length[x][y] = dist
  m_matrix[x][y] = matrix[x][y]

  if x > 0 and matrix[x][y] in '|JL':
    explore(x-1, y, dist+1)

  if x < len(matrix) - 1 and matrix[x][y] in '|7F':
    explore(x+1, y, dist+1)

  if y > 0 and matrix[x][y] in 'J7-':
    explore(x, y-1, dist+1)

  if y < len(matrix[0]) - 1 and matrix[x][y] in 'FL-':
    explore(x, y+1, dist+1)

spos = (start, matrix[start].index('S'))
m_length[spos[0]][spos[1]] = 0

s_type = 0
if spos[0] > 0 and matrix[spos[0] - 1][spos[1]] in 'F7|':
  explore(spos[0] - 1, spos[1], 1)
  s_type += 1

if spos[0] < len(matrix) - 1 and matrix[spos[0] + 1][spos[1]] in 'LJ|':
  explore(spos[0] + 1, spos[1], 1)
  s_type += 2

if spos[1] > 0 and matrix[spos[0]][spos[1] - 1] in 'FL-':
  explore(spos[0], spos[1] - 1, 1)
  s_type += 4

if spos[1] < len(matrix[0]) - 1 and matrix[spos[0]][spos[1] + 1] in '7J-':
  explore(spos[0], spos[1] + 1, 1)
  s_type += 8

if s_type == 3: matrix[spos[0]] = matrix[spos[0]].replace('S', '|')
elif s_type == 5: matrix[spos[0]] = matrix[spos[0]].replace('S', 'J')
elif s_type == 9: matrix[spos[0]] = matrix[spos[0]].replace('S', 'L')
elif s_type == 6: matrix[spos[0]] = matrix[spos[0]].replace('S', '7')
elif s_type == 10: matrix[spos[0]] = matrix[spos[0]].replace('S', 'F')
elif s_type == 12: matrix[spos[0]] = matrix[spos[0]].replace('S', '-')

m_matrix[spos[0]][spos[1]] = matrix[spos[0]][spos[1]]

mmax = 0
for i in m_length:
  if max(i) > mmax:
    mmax = max(i)

print(mmax)

for kl, line in enumerate(m_matrix):
  inside = False
  prev = '.'
  for kc, char in enumerate(line):
    if char in '|FLJ7':
      if char == '7' and prev == 'L':
        continue
      if char == 'J' and prev == 'F':
        continue
      prev = char
      inside = not inside

    if char == '.':
      if inside: i_matrix[kl][kc] = 1

print_m(m_matrix)
print_m(i_matrix)

suml = 0
for line in i_matrix:
  suml += sum(line)

print(suml)

