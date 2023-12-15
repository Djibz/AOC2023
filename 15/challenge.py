def hash_string(string, cur=0): return cur if len(string) == 0 else hash_string(string[1:], ((cur + ord(string[0])) * 17) % 256)

with open('./15/input.txt', 'r') as input: print(sum([hash_string(p) for p in input.read()[:-1].split(',')]))

with open('./15/input.txt', 'r') as input:
  boxes = dict()
  for i in range(256):
    boxes[i] = []

  def remove_from_box(b_nb, label):
    for k, v in enumerate(boxes[b_nb]):
      if v[0] == label:
        boxes[b_nb].pop(k)
        break

  def add_in_box(b_nb, label, value):
    for k, v in enumerate(boxes[b_nb]):
      if v[0] == label:
        boxes[b_nb][k] = (label, value)
        return
    boxes[b_nb].append((label, value))

  for part in input.read()[:-1].split(','):
    if '-' in part:
      label = part.split('-')[0]
      remove_from_box(hash_string(label), label)

    else:
      label = part.split('=')[0]
      value = part.split('=')[1]
      add_in_box(hash_string(label), label, value)

  total = 0
  for k, v in boxes.items():
    for nl, lense in enumerate(v):
      total += (1 + k) * (1+nl) * int(lense[1])

  print(total)

