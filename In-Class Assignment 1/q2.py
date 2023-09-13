import numpy as np
import pyromat as pm

water = pm.get('mp.H2O')

m_dot = 26 #kg/s
p_in = 60 #Bar
t_in = 600 + 273.15
h_in = water.h(T=t_in, p=p_in)
print(h_in)


p_out = 5 #Bar
t_out = 200 + 273.15
v_out = 180 #m/s
W_dot_out = 20350 #kW
h_out = water.h(T=t_out, p=p_out)
print(h_out)
KE_dot_out = 0.5 * m_dot * v_out**2 / 1000
Q_dot = m_dot * (h_out - h_in) / 1000 - KE_dot_out + W_dot_out

print(Q_dot)

