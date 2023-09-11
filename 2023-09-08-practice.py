import numpy as np
import pyromat as pm
import matplotlib.pyplot as plt

water = pm.get('mp.H2O')
t_1 = 273.15 + 40 #Kelvin
vol = 50 / 1000 #m^3
p_1 = 2 # Bar
v_1 = 1 / water.d(T=t_1, p = p_1) # 1/density, m^3/kg
print(v_1)

# Get density, mass, and enthalpy from the above properties.
den = water.d(T=t_1, p=p_1)
mass = vol * den
h_1 = water.h(T=t_1, p=p_1)
print(mass)



# Get the final enthalpy after vapourization of all substatnces
t_2 = water.T(p=p_1, x=1)
h_2 = water.h(p=p_1, x=1)
delta_h = mass * (h_2 - h_1)


print(delta_h, t_2)

fig_1 = plt.figure(1)
ax1 = fig_1.add_subplot(111)
ax1.set_xlabel('Specific Volume, v (m^3/kg)')
ax1.set_ylabel('Temperature, T (K)')

Tt,pt = water.triple()
Tc,pc = water.critical()
T = np.arange(Tt,Tc,2.5)
p = water.ps(T)
dL,dV = water.ds(T=T)
ax1.plot(1/dL,p,'k')
ax1.plot(1/dV,p,'k')

ax1.set_xscale('log')
# ax1.set_yscale('log')
ax1.set_xlim([5e-4, 1])
ax1.set_ylim([.01,400.])

ax1.plot(v_1, t_1, 'k')

plt.show()
