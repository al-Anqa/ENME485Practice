import numpy as np
import pyromat as pm

water = pm.get('mp.H2O')

p=100
t_1 = 800 + 273.15
water = pm.get('mp.H2O')


s_1 = water.s(p=p, T=t_1, quality = True)
print(s_1)
