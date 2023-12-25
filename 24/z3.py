from z3 import *

r = Real('r')
s = Real('s')
t = Real('t')
uu = Real('u')
v = Real('v')
w = Real('w')
x = Real('x')
y = Real('y')
z = Real('z')

sol = Solver()

sol.add(uu+x*r==19-r)
sol.add(v+y*r == 13+r)
sol.add(w+z*r==30-2*r)
sol.add(uu+x*s == 18-s)
sol.add(v+y*s == 19-s)
sol.add(w+z*s == 22-2*s)
sol.add(uu+x*t == 20-2*t)
sol.add(v+y*t== 25-2*t)
sol.add(w+z*t == 34 -4*t)

sol.check()