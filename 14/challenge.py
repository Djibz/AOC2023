import numpy as np
import re

lines = []

with open('./14/input.txt', 'r') as input:
    for line in input:
        lines.append(line[:-1])

nparr = np.array([list(x) for x in lines])
transpose = [''.join(x) for x in nparr.transpose().tolist()]

print(transpose)

total = 0
for col in transpose:
    parts = col.split('#')
    new_parts = [ sorted(p,) for p in parts]
    new_parts = [('O' * len(re.findall(r'O', p))) + ('.' * (len(p) - len(re.findall(r'O', p)))) for p in parts]
    for i, c in enumerate(list(reversed('#'.join(new_parts)))):
        if c == "O": total += i + 1

print(total)