import numpy as np

patterns = []

def edit_distance(a, b):
  count = 0
  if len(a) != len(b):
    return -1
  for i in range(len(a)):
    for j in range(len(a[i])):
      if a[i][j] != b[i][j]:
        count += 1
  return count

def has_1edit_in(a, list):
  for l in list:
    if edit_distance([a], [l]) == 1:
      return True
  return False

with open('./13/input.txt', 'r') as input:

  print("Part 1")
  curr_pat = []
  for line in input:
    if line[:-1] == '':
      patterns.append(curr_pat)
      curr_pat = []
      continue
    curr_pat.append(line[:-1])

total = 0
for k, pattern in enumerate(patterns):

  if has_1edit_in(pattern[0], pattern[1:]) or pattern[0] in pattern[1:]:
    for i in range(0, len(pattern)):
      if edit_distance(pattern[0:i+1], list(reversed(pattern[i+1:2*(i+1)]))) == 1:
        total += len(pattern[:i+1]) * 100
        print(len(pattern[:i+1]) * 100)

  if has_1edit_in(pattern[-1], pattern[:-1]) or pattern[-1] in pattern[:-1]:
    for i in range(0, len(pattern)):
      if edit_distance(pattern[-i-1:], list(reversed(pattern[2*(-i-1):-i-1]))) == 1:
        total += len(pattern[:-i-1]) * 100

  nparr = np.array([list(x) for x in pattern])
  transpose = [''.join(x) for x in nparr.transpose().tolist()]

  if has_1edit_in(transpose[0], transpose[1:]) or transpose[0] in transpose[1:]:
    for i in range(0, len(transpose)):
      if edit_distance(transpose[0:i+1], list(reversed(transpose[i+1:2*(i+1)]))) == 1:
        total += len(transpose[0:i+1]) 

  if has_1edit_in(transpose[-1], transpose[:-1]) or transpose[-1] in transpose[:-1]:
    for i in range(0, len(transpose)):
      if edit_distance(transpose[-i-1:], list(reversed(transpose[2*(-i-1):-i-1]))) == 1:
        total += len(transpose[:-i-1])


print(total)