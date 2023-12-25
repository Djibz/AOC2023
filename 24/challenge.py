import re
import matplotlib.pyplot as plt
import plotly.express as px

hs = []

with open('./24/input.txt') as input:
  for line in input:
    hs.append([int(x) for x in re.findall(r'-?\d+', line)])

test_area = (7, 27)
test_area = (200000000000000, 400000000000000)

def polynom(h):
  a = h[4] / h[3]
  return a, h[1] - (h[0] * a)

def intersectionXY(h1, h2):
  a1, b1 = polynom(h1)
  a2, b2 = polynom(h2)

  a = a1 - a2
  b = b2 - b1
  if a == 0: return (None, None)
  return b / a, (a1*(b/a)+b1)

x, y = intersectionXY(hs[0], hs[1])

total = 0
intersections = set()

for i in range(len(hs)):
  for j in range(i+1, len(hs)):
    s1 = hs[i]  
    s2 = hs[j]
    x, y = intersectionXY(s1, s2)
    a, b = polynom(s1)
    a2, b2 = polynom(s1)
    if x == None: continue
    t1 = (x - s1[0]) / s1[3]
    t2 = (x - s2[0]) / s2[3]
    if t1 < 0 or t2 < 0: continue
    if test_area[0] <= x <= test_area[1] and test_area[0] <= y <= test_area[1]:
      intersections.add((x, y, t1, t2))
      total += 1

print(f"Part 1 : {total}")
# print(intersections)

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
# Creating plot
ax.scatter3D([x[0] for x in hs], [x[1] for x in hs], [x[2] for x in hs], color = "green")
plt.show()

# df = px.data.iris()
# fig = px.scatter_3d([x[0] for x in hs], [x[1] for x in hs], [x[2] for x in hs])
# fig.show()