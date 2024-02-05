import pyromat as pm

pm.config['unit_pressure'] = 'MPa'
pm.config['unit_temperature'] = 'C'

water = pm.get('mp.H2O')


p_1= 0.5

s_1 = water.ss(p=p_1)[0]
print(s_1)

s_6 = s_1
p_6 = 15
t_6 = water.T(s=s_6, p=p_6)
print(t_6)