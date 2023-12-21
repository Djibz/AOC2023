import re

broadcast = []
modules = dict()
ff = dict()
conj = dict()

with open('./20/input.txt') as input:
  for line in input:
    l, r = line.split('->')
    outs = re.findall(r'\w+', r)
    if l == "broadcaster ":
      broadcast = outs
      continue
    name = l[1:-1]
    modules[name] = outs
    if l[0] == '%':
      ff[name] = 0
    if l[0] == '&':
      conj[name] = dict()

for k, v in modules.items():
  for out in v:
    if out in conj:
      conj[out][k] = 0

fifo = []

def send_signal(src, dest, force):
  if dest in ff and force == 0:
    if ff[dest] == 1:
      ff[dest] = 0
      for m in modules[dest]:
        fifo.append((dest, m, 0))
    else:
      ff[dest] = 1
      for m in modules[dest]:
        fifo.append((dest, m, 1))
  
  if dest in conj:
    conj[dest][src] = force
    if min(conj[dest].values()) == 1:
      for m in modules[dest]:
        fifo.append((dest, m, 0))
    else:
      for m in modules[dest]:
        fifo.append((dest, m, 1))

totalH = 0
totalL = 0

for i in range(1000):
  totalL += 1
  for o in broadcast:
    fifo.append(('broadcast', o, 0))

  while len(fifo) != 0:
    src, dest, force = fifo.pop(0)
    send_signal(src, dest, force)
    if force == 0: totalL += 1
    else: totalH += 1


print(totalH, totalL)
print(totalH * totalL)

i = 0
while True:
  for o in broadcast:
    fifo.append(('broadcast', o, 0))

  while len(fifo) != 0:
    src, dest, force = fifo.pop(0)
    if dest == 'rx' and force == 0:
      print(i)
      exit()
    send_signal(src, dest, force)

  i += 1
  if i % 100000 == 0:
    print(f"{i//100000}M")
    print(conj['hd'])
    print(conj['tn'])
    print(conj['vc'])
    print(conj['jx'])
