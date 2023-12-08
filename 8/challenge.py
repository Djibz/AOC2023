import re

nodes = dict()
from_left = dict()
from_right = dict()
with open('./8/example3.txt', 'r') as input:

  seq = input.readline()[:-1]
  input.readline()

  for line in input:
    (start, left, right) = re.findall(r'^(\w\w\w) = \((\w\w\w), (\w\w\w)\)$', line)[0]
    nodes[start] = (left, right)
    last = start

current = 'AAA'
steps = 0
#while current != 'ZZZ':
#  if (steps % 10000000 == 0):
#    print(steps)
#  current = nodes[current][0 if seq[steps % len(seq)] == 'L' else 1]
#  steps += 1

currents = []
for key in nodes:
  if key[2] == 'A':
    currents.append(key)

def count_z(list):
  count = 0
  for a in list:
    if a[2] == 'Z':
      count += 1
  return count

print(currents)
while not count_z(currents) == len(currents):
  if (count_z(currents) > 3):
    print(count_z(currents))
  for i in range(len(currents)):
    currents[i] = nodes[currents[i]][0 if seq[steps % len(seq)] == 'L' else 1]
  steps += 1

print(currents)

print(steps)