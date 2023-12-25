import networkx as nx
import matplotlib.pyplot as plt
import re

con = []

with open('./25/input.txt') as input:
  for line in input:
    parts = re.findall(r'\w+', line)
    for part in parts[1:]:
      con.append((parts[0], part))

# print(con)

# G = nx.Graph()
# G.add_edges_from(con)
# nx.draw(G, with_labels=True)
# plt.show()

# rxt - bqq
# qrx - btp
# vfx - bgl

con.remove(('rxt', 'bqq'))
# con.remove(('bqq', 'rxt'))
# con.remove(('qxr', 'btp'))
con.remove(('btp', 'qxr'))
con.remove(('vfx', 'bgl'))
# con.remove(('bgl', 'vfx'))

went = []

def lenght_from(node, went):
  went.append(node)

  count = 1

  for c in con:
    if node in c:
      for n in c:
        if n not in went:
          count += lenght_from(n, went)

  return count

a = lenght_from('rxt', went)
b = lenght_from('bqq', went)

print(a)
print(b)
print(a*b)