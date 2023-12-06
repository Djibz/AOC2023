total = 1
time = 71530
dist = 940200
time = 52947594
dist = 426137412791216

total = 0
for j in range(time):
    if j * (time - j) > dist:
        total += 1

print(total)
