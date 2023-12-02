import re

with open('./2/input.txt', 'r') as input:

  total = 0
  total2 = 0

  for line in input:

    groups = re.findall(r'[\d\w ,]+', line)
    ID = int(re.findall(r'Game (\d+)', groups.pop(0))[0])

    good = True

    game_counter_min = dict()
    game_counter_min['green'] = 0
    game_counter_min['red'] = 0
    game_counter_min['blue'] = 0
    for part in groups:
      elements = re.findall(r'(\d+) (\w+)', part)
      part_counter = dict()
      part_counter['green'] = 0
      part_counter['red'] = 0
      part_counter['blue'] = 0
      
      for elem in elements:
        n = int(elem[0])
        k = elem[1]
        part_counter[k] += n

        if n > game_counter_min[k]:
          game_counter_min[k] = n

      print(part_counter)
      if part_counter['red'] > 12 or part_counter['green'] > 13 or part_counter['blue'] > 14:
        good = False
      
    if (good):
      total += ID

    power = (game_counter_min['green']) * (game_counter_min['red']) * (game_counter_min['blue'])
    print(power)
    total2 += power

  print(f'Part1 total : {total}')
  print(f'Part2 total : {total2}')