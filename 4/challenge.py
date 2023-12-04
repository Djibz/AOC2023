import re

def numbers_of_str(string):
  return [int(i) for i in re.findall(r'\d+', string)]

with open('./4/input.txt', 'r') as input:

  total = 0
  cards_wins = dict()

  for line in input:
    total_line = 0
    count_wins = 0 # Part2
    (winning, got) = line.split('|')
    id = numbers_of_str(winning)[0]
    winning = numbers_of_str(winning)[1:]
    got = numbers_of_str(got)

    for n in got:
      if n in winning:
        count_wins += 1 # Part2
        if total_line == 0:
          total_line = 1
        else: total_line *= 2
    
    total += total_line
    cards_wins[id] = count_wins
  
  print(f"Part1 : {total}")

  print(cards_wins)

  cards_counter = [1 for _ in range(len(cards_wins))]

  for cid in range(1, len(cards_wins)+1):
    for i in range(1, cards_wins[cid]+1):
      cards_counter[cid-1+i] += cards_counter[cid-1]

  print(sum(cards_counter))