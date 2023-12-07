import re

cards = '1AKQJT98765432'

hands_values = dict()
hands_values[0] = []
hands_values[1] = []
hands_values[2] = []
hands_values[3] = []
hands_values[4] = []
hands_values[5] = []
hands_values[6] = []

nb_lines = 0
with open('./7/example.txt', 'r') as input:

  print("Part 1")

  for line in input:
    nb_lines += 1

    (hand, bid) = line.split()
    
    vwin = 0
    for card in cards:
      matches = re.findall(fr'{card}', hand)
      
      if len(matches) == 5:
        vwin = 6
        break

      if len(matches) == 4:
        vwin = 5
        break

      if len(matches) == 3:
        if vwin == 1: vwin = 4
        else: vwin = 3

      if len(matches) == 2:
        if vwin == 3: vwin = 4
        elif vwin == 1: vwin = 2
        else: vwin = 1

    hands_values[vwin].append((hand, bid))

print(hands_values)

def hand_v(hand):
  total = 0
  for i in range(5):
    total += (len(cards) - cards.index(hand[i])) * (6 - (i+1) * 5)

  return total

#for v, k in hands_values.items():
  k.sort(key= lambda x: hand_v(x[0]), reverse=False)

total = 0
count = 1
for k, v in hands_values.items():

  while len(v) != 0:
    smaller = ('11111', '0')
    for i in range(0, 5):
      for h in v:
        if h[0][0:i] == smaller[0][0:i]:
          if cards.index(h[0][i]) > cards.index(smaller[0][i]):
            smaller = h

    total += count * int(smaller[1])
    count += 1
    v.remove(smaller)

print(total)
