import re

def count_group(place, line):
  group_passed = 0
  in_group = False
  count_size = 0
  for i in range(len(line)):
    if (line[i] == '#'):
      in_group = True
      if group_passed == place:
        count_size += 1

    if line[i] != '#' and in_group:
      group_passed += 1
      in_group = False

  return count_size

def check_good(line, groups):
  for k, g in enumerate(groups):
    if count_group(k, line) != g:
      return False
  return True

def place_groups(line, groups, to_place):
  new_line = list(line)
  if to_place == 0:
    if check_good(line, groups):
      return [1]
    return [0]
    return str(line).replace('?', '.')
  
  results = []

  for i in range(len(line)):
    if new_line[i] == '?':
      new_line[i] = '#'
      results += place_groups(''.join(new_line), groups, to_place-1)
      new_line[i] = '.'

  return results

total = 0

with open('./12/input.txt', 'r') as input:

  print("Part 1")
  total = 0
  for line in input:
    (slist, groups) = line.split()
    groups = [int(i) for i in re.findall(r'[0-9]+', line)]
    to_place = sum(groups) - len(re.findall(r'#', slist))
    total += sum(place_groups(slist, groups, to_place))

print(total)