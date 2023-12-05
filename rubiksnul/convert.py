import re

with open('./ortega2.txt') as input:
    for line in input:
        actions = line.split()
        serializeds = []

        for action in actions:
            if len(action) == 1:angle = 'Clockwise'
            elif action[1] == "'": angle = 'AntiClockwise'
            else: angle = 'HalfTurn'

            if action[0] == 'R': face = "East"
            elif action[0] == 'F': face = 'South'
            elif action[0] == 'U': face = 'Top'
            elif action[0] == 'B': face = 'Bottom'
            #elif action[0] == 'F': face = 'South'
            else: face = 'West'

            serializeds.append(f'({face}, {angle})')

        print('; '.join(serializeds))