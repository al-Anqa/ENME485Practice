# ENME 485 In-Class Assignment 1
# Ahmed Almousawi, 30140399, ahmed.almousawi1@ucalgary.ca
# Required libraries: Numpy, Matplotlib, Pyromat
# Remember to close the first plot to see the second one!

import numpy as np
import pyromat as pm
import matplotlib.pyplot as plt

pm.config['unit_temperature'] = 'K'
pm.config['unit_pressure'] = 'kPa'

R134a = pm.get("mp.C2H2F4")

# State 1 - Condensor Inlet/Compressor Outlet
p_1 = 800 #kPa
t_1 = [35 + 273.15] # Kelvin
h_1 = R134a.h(p=p_1, T=t_1)
s_1 = R134a.s(p=p_1, T=t_1)
m_dot = 0.018 # kg/s

# State 2 - Condensor Output/Expansion Valve Inlet
p_2 = 800 #kPa
t_2 = R134a.T(p=p_2, x=0)
h_2 = R134a.h(p=p_2, x=0)
s_2 = R134a.s(p=p_2, x=0)

print(t_2, h_2)


# State 3 - Expansion Valve Output/Evaporater Inlet
p_3 = 100 #kPa
h_3 = h_2
t_3 = R134a.T(p=p_3, h=h_3, quality=True)
x_3 = t_3[1]
t_3 = t_3[0]
s_3 = R134a.s(p=p_3, x=x_3)
inlet_entropy = s_3 * m_dot
print(f'The entropy at evaporator inlet is {inlet_entropy}')

# State 4 - Evaporator Outlet/Compressor Inlet
p_4 = p_3
t_4 = R134a.T(p=p_4, x=1)
h_4 = R134a.h(p=p_4, x=1)
s_4 = R134a.s(p=p_4, x=1)

q_l = (h_4 - h_3) * m_dot
print(f'The Q_h value is {q_l}')

q_h = (h_1 - h_2) * m_dot
print(f'The Q_h value is {q_h}')

coeff_of_performance = q_h / (q_h-q_l)
print(f'The coefficient of performance is {coeff_of_performance}')


plt.figure(1)

T_trip, p_trip = R134a.triple()
T_crit, p_crit = R134a.critical()

T = np.linspace(T_trip, T_crit, 1000)
p = R134a.ps(T=T)
s = R134a.ss(T=T)

plt.plot(s[0], T, 'k')
plt.plot(s[1], T, 'k')

# Now, we plot the lines on the T-s diagram
x=[s_1, s_2, s_3, s_4, s_1]
y=[np.array(t_1), t_2, t_3, t_4, t_1]
plt.plot(x, y, 'r')
# Now add labels
plt.xlabel("Entropy, S, [kJ / kg * K]")
plt.ylabel("Temperature, T, [K]")

# Finally, save and show
plt.savefig('In-Class Assignment 2\Q2 Temperature - Entropy Diagram.pdf')
plt.show()