# ENME 485 In-Class Assignment 1
# Ahmed Almousawi, 30140399, ahmed.almousawi1@ucalgary.ca
# Required libraries: Numpy, Matplotlib, Pyromat
# Remember to close the first plot to see the second one!

import numpy as np
import pyromat as pm
import matplotlib.pyplot as plt

water = pm.get('mp.H2O')

# This section is just defining the given values and using them to get entropy and enthalpy

m_dot = 26 # kg/s
p_in = 60 # Bar
t_in = 600 + 273.15 # K
s_in = water.s(T=t_in, p=p_in) # kJ/kg*K
h_in = water.h(T=t_in, p=p_in) # kJ/kg
print(h_in)

p_out = 5 # Bar
t_out = 200 + 273.15 # K
v_out = 180 # m/s
W_dot_out = 20350 # kW
s_out = water.s(T=t_out, p=p_out) # kJ/kg*K
h_out = water.h(T=t_out, p=p_out) # kJ/kg
print(h_out)
KE_dot_out = 0.5 * m_dot * v_out**2 / 1000 #kJ/kg
print(KE_dot_out)

# Q - W = m_out * (h_out + V_out^2/2000 + g*z_out) - m_in * (h_in + V_in^2/2000 + g*z_in)
# V_in = 0, z_in = z_out, so equation becomes:
# Q = m * (h_out) + KE - m * (h_in)

Q_dot = m_dot * (h_out - h_in) + KE_dot_out + W_dot_out

print(Q_dot)

# Plotting 
# Plotting the dome
plt.figure(1)

T_trip, p_trip = water.triple()
T_crit, p_crit = water.critical()

p = np.linspace(p_trip, p_crit, 1000)
T = water.Ts(p=p)
s = water.ss(p=p)

plt.plot(s[0], T, 'k')
plt.plot(s[1], T, 'k')

# Now, we plot the lines on the T-s diagram
x=[s_in, s_out]
y=[t_in, t_out]
plt.plot(x, y, 'r')
# Now add labels
plt.xlabel("Entropy, S, [kJ / kg * K]")
plt.ylabel("Temperature, T, [K]")

# Finally, save and show
plt.savefig('In-Class Assignment 1\Q2 Temperature - Entropy Diagram.pdf')
plt.show()

# Now, we need to plot the change of Q against outlet velocity
# First, lets get the arrays. We call it Q_compare, v_compare, and KE_compare.
v_compare = np.linspace(0,800, 20)
KE_compare = 0.5 * m_dot * v_compare**2 / 1000

Q_compare = m_dot * (h_out - h_in) + KE_compare + W_dot_out
print(KE_compare, Q_compare)

# Now, we define our figure and plot.
plt.figure(2)
plt.xlabel("Velocity, v, [m/s]")
plt.ylabel("Heat Transfer, Q_dot, [kW]")

plt.plot(v_compare, Q_compare)
# Finally, save and show
plt.savefig('In-Class Assignment 1\Q2 Heat Transfer - Velocity Diagram.pdf')
plt.show()