import numpy as np

patterns = []

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

  if (pattern[0]) in pattern[1:]:
    for i in range(0, len(pattern)):
      if pattern[0:i+1] == list(reversed(pattern[i+1:2*(i+1)])):
        total += len(pattern[:i+1]) * 100

  if (pattern[-1]) in pattern[:-1]:
    for i in range(0, len(pattern)):
      if pattern[-i-1:] == list(reversed(pattern[2*(-i-1):-i-1])):
        total += len(pattern[:-i-1]) * 100

  nparr = np.array([list(x) for x in pattern])
  transpose = [''.join(x) for x in nparr.transpose().tolist()]

  if (transpose[0]) in transpose[1:]:
    for i in range(0, len(transpose)):
      if transpose[0:i+1] == list(reversed(transpose[i+1:2*(i+1)])):
        total += len(transpose[0:i+1]) 

  if (transpose[-1]) in transpose[:-1]:
    for i in range(0, len(transpose)):
      if transpose[-i-1:] == list(reversed(transpose[2*(-i-1):-i-1])):
        total += len(transpose[:-i-1])


print(total)