import numpy as np

schematic = []

with open('./3/input.txt', 'r') as input:
    for l in input:
        schematic.append(l)

total = 0
width = len(schematic[0])-2

for i in range(len(schematic)):
    number = ''
    is_validate = False
    total_line = 0
    for j in range(len(schematic[0])):
        if schematic[i][j] in '0123456789':
            number += schematic[i][j]

            if (j > 0 and schematic[i][j-1] not in '0123456789.\n'):
                is_validate = True
            if (j < width and schematic[i][j+1] not in '0123456789.\n'):
                is_validate = True

            if (i > 0 and schematic[i-1][j] not in '0123456789.\n'):
                is_validate = True
            if (i < len(schematic)-1 and schematic[i+1][j] not in '0123456789.\n'):
                is_validate = True

            if (i > 0 and j > 0 and schematic[i-1][j-1] not in '0123456789.\n'):
                is_validate = True
            if (i < len(schematic)-1 and j > 0 and schematic[i+1][j-1] not in '0123456789.\n'):
                is_validate = True

            if (i > 0 and j < width and schematic[i-1][j+1] not in '0123456789.\n'):
                is_validate = True
            if (i < len(schematic)-1 and j < width and schematic[i+1][j+1] not in '0123456789.\n'):
                is_validate = True

        if schematic[i][j] not in '0123456789':
            if is_validate:
                total += int(number)
                total_line += int(number)
            
            number = ''
            is_validate = False

print(total)

def total_number(i, j):
    number = schematic[i][j]

    index = j-1
    while index >= 0 and schematic[i][index] in '0123456789':
        number = schematic[i][index] + number
        index -=1
    
    index = j+1
    while index <= width and schematic[i][index] in '0123456789':
        number += schematic[i][index]
        index += 1
    
    return int(number)

total = 0
for i in range(len(schematic)):
    for j in range(len(schematic[0])):
        if schematic[i][j] in '*':
            numbers = []
            if (j > 0 and schematic[i][j-1] in '0123456789'):
                numbers.append(total_number(i, j-1))
            if (j < width and schematic[i][j+1] in '0123456789'):
                numbers.append(total_number(i, j+1))

            if (i > 0 and schematic[i-1][j] in '0123456789'):
                numbers.append(total_number(i-1, j))
            if (i < len(schematic)-1 and schematic[i+1][j] in '0123456789'):
                numbers.append(total_number(i+1, j))

            if (i > 0 and j > 0 and schematic[i-1][j-1] in '0123456789'):
                numbers.append(total_number(i-1, j-1))
            if (i < len(schematic)-1 and j > 0 and schematic[i+1][j-1] in '0123456789'):
                numbers.append(total_number(i+1, j-1))

            if (i > 0 and j < width and schematic[i-1][j+1] in '0123456789'):
                numbers.append(total_number(i-1, j+1))
            if (i < len(schematic)-1 and j < width and schematic[i+1][j+1] in '0123456789'):
                numbers.append(total_number(i+1, j+1))

            numbers = list(set(numbers))

            if len(numbers) == 2:
                total += numbers[0] * numbers[1]

print(total)