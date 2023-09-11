import pyromat as pm

water = pm.get('mp.H2O')
pm.config
p = 1 # Bar
h = water.h(p=p, e=2000)
v = water.v(p=p, e=2000)
s = water.s(p=p, e=2000, quality=True)

print(h, v, s[0], s[1])