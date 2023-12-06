import re

with open('./6/input.txt', 'r') as input:

    print("Part 1")

  
    times = [int(i) for i in re.findall(r'[0-9]+', input.readline())]
    dist = [int(i) for i in re.findall(r'[0-9]+', input.readline())]

total = 1
for i in range(len(times)):
    total_wins = 0

    for j in range(times[i]):
        if j * (times[i] - j) > dist[i]:
            total_wins += 1
    
    total *= total_wins

print(total)
