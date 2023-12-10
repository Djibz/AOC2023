import re

total = 0
total_b = 0

def next_step(seq):
  n = []
  for i in range(len(seq)-1):
    n.append(seq[i+1] - seq[i])
  
  return n

with open('./9/input.txt', 'r') as input:
  line_c = 0
  for line in input:
    
    numbers = [int(i) for i in re.findall(r'-?\d+', line)]
    all_steps = [numbers]
    current = numbers
    while len(current) > 0 and set(current) != set([0]):
      next = next_step(current)
      all_steps.append(next)
      current = next

    #if len(current) == 0:
    #  all_steps.pop()

    all_steps[-1].append(0)

    for i in range(len(all_steps)-1):
      all_steps[len(all_steps)- 2 - i].append(all_steps[len(all_steps)- 1 - i][-1] + all_steps[len(all_steps)- 2 - i][-1])
    
    total += all_steps[0][-1]
      

    line_c += 1

print(total)