import re
import numpy as np
import math

inputs = []
first = True
wf = dict()
parts = []

with open('./19/example.txt', 'r') as input:
    for line in input:
      if line == '\n':
         first = False
         continue

      if first:
        #wf.append()
        (name, p) = re.findall(r'^(.*?)\{(.*)\}$', line)[0]
        wf[name] = p.split(',')

      if not first:
        (x, m, a, s) = re.findall(r'\d+', line)
        part = dict()
        part['x'] = x
        part['m'] = m
        part['a'] = a
        part['s'] = s
        parts.append(part)

def part_accepted(part, wf_name='in'):
  for w in wf[wf_name]:
    if '<' in w:
      (rest, res) = w.split(':')
      (l, n) = rest.split('<')
      if int(part[l]) < int(n):
        next_w = res
        break
    elif '>' in w:
      (rest, res) = w.split(':')
      (l, n) = rest.split('>')
      if int(part[l]) > int(n):
        next_w = res
        break
    else:
      next_w = w
      break

  if next_w == 'A':
    return True
  if next_w == 'R':
    return False

  return part_accepted(part, wf_name=next_w)

total = 0
for p in parts:
  if part_accepted(p):
    total += sum([int(x) for x in p.values()])

print(total)

ranges = dict()


def wins_ranges(wf_k):
  rs = dict()
  rs['x'] = (1, 4000)
  rs['a'] = (1, 4000)
  rs['m'] = (1, 4000)
  rs['s'] = (1, 4000)
  for w in wf[wf_k]:
    if '<' in w:
      (rest, res) = w.split(':')
      (l, n) = rest.split('<')
      if int(part[l]) < int(n):
        if res == 'A':
          rs[l]  = (1, int(n)-1)
        if res == 'R':
          rs[l]  = (int(n), 4000)
    elif '>' in w:
      (rest, res) = w.split(':')
      (l, n) = rest.split('>')
      if int(part[l]) > int(n):
        if res == 'A':
          rs[l]  = (int(n)+1, 4000)
        if res == 'R':
          rs[l]  = (1, int(n))

for k, v in wf.items():
  if v[-1] == 'R':
    continue