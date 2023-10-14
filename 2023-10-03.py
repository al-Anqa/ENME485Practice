import pyromat as pm

pm.config['unit_pressure'] = 'MPa'
pm.config['unit_temperature'] = 'C'

water = pm.get('mp.H2O')


p_1= 2

t_1 = water.Ts(p=p_1)
print(t_1)