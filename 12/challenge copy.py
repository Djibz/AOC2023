import re
from functools import cache
from typing import List, Tuple

@cache
def count_valid_cached(springs: str, groups: Tuple[int]):
    if len(springs) == 0:
        if len(groups) == 0:
            return 1
        else:
            return 0

    curr = springs[0]
    if curr == "#":
        if len(groups) == 0 or len(springs) < groups[0]:
            return 0

        if "." in springs[0 : groups[0]]:
            return 0

        if springs[groups[0] :].startswith("#"):
            return 0

        if len(springs) > groups[0]:
            if springs[groups[0]] == "?":
                return count_valid_cached(springs[groups[0] + 1 :].lstrip("."), groups[1:])

        return count_valid_cached(springs[groups[0] :].lstrip("."), groups[1:])
    elif curr == ".":
        return count_valid_cached(springs.lstrip("."), groups)
    elif curr == "?":
        return count_valid_cached("#" + springs[1:], groups) + count_valid_cached("." + springs[1:], groups)


total = 0

with open('./12/input.txt', 'r') as input:

  print("Part 1")
  total = 0
  for line in input:
    (slist, groups) = line.split()
    groups = [int(i) for i in re.findall(r'[0-9]+', line)]

    total += count_valid_cached('?'.join([slist] * 5), tuple(groups * 5))

print(total)