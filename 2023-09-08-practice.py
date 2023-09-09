import numpy as np
import pyromat as pm
import matplotlib.pyplot as plt

water = pm.get('mp.H2O')
temp_1 = 273.15 + 40 #Kelvin
vol = 50 / 1000 #m^3
p_1 = 2 # Bar
v_1 = 1 / water.d(T=temp_1, p = p_1) # 1/density, m^3/kg

# Get density, mass, and enthalpy from the above properties.
den = water.d(T=temp_1, p=p_1)
mass = vol * den
enthalpy_i = water.h(T=temp_1, p=p_1)
print(mass)



# Get the final enthalpy after vapourization of all substatnces
temp_2 = 100 + 273.15
enthalpy_f = water.h(T=temp_2, p=p_1, x=1)
delta_h = enthalpy_f - enthalpy_i

print(delta_h)

fig_1 = plt.figure(1)
ax1 = fig_1.add_subplot(111)
ax1.set_xlabel('Specific Volume, v (m^3/kg)')
ax1.set_ylabel('Temperature, T (K)')

Tt,pt = water.triple()
Tc,pc = water.critical()
T = np.arange(Tt,Tc,2.5)
p = water.ps(T)
dL,dV = water.ds(T=T)
ax1.plot(1./dL,p,'k')
ax1.plot(1./dV,p,'k')

ax1.set_xscale('log')
# ax1.set_yscale('log')
ax1.set_xlim([5e-4, 50])
ax1.set_ylim([.01,300.])

plt.show()
