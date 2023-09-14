# ENME 485 In-Class Assignment 1
# Ahmed Almousawi, 30140399, ahmed.almousawi1@ucalgary.ca
# Required libraries: Pyromat
# Remember to close the first plot to see the second one!
import pyromat as pm

water = pm.get('mp.H2O')


p_1 = 2
x_1 = 0.7

water = pm.get('mp.H2O')

t_1 = water.T(p=p_1, x=0.7) - 273.15
h_1 = water.h(p=p_1, x=0.7)
e_1 = water.e(p=p_1, x=0.7)
s_1 = water.s(p=p_1, x=0.7)
v_1 = 1 / water.d(p=p_1, x=0.7)

print(t_1, h_1, e_1, s_1, v_1)

t_2 = 150 + 273.15
h_2 = 1800
e_2 = water.e(T = t_2, h=h_2)
s_2 = water.s(T = t_2, h=h_2, quality = True)
v_2 = 1 / water.d(T = t_2, h=h_2)

print(t_2, h_2, e_2, s_2, v_2)

p_3 = 9.5
t_3 = water.T(p=p_3, x=0.0) - 273.15
h_3 = water.h(p=p_3, x=0.0)
e_3 = water.e(p=p_3, x=0.0)
s_3 = water.s(p=p_3, x=0.0)
v_3 = 1 / water.d(p=p_3, x=0.0)

print(t_3, h_3, e_3, s_3, v_3)

p_4 = 8
h_4 = 3162.2
t_4 = water.T(p=p_4, h=h_4) - 273.15
e_4 = water.e(p=p_4, h=h_4)
s_4 = water.s(p=p_4, h=h_4, quality = True)
v_4 = 1 / water.d(p=p_4, h=h_4)

print(t_4, h_4, e_4, s_4, v_4)

t_5 = 520 + 273.15
p_5 = 60
h_5 = water.h(T=t_5, p=p_5)
e_5 = water.e(T=t_5, p=p_5)
s_5 = water.s(T=t_5, p=p_5, quality = True)
v_5 = 1 / water.d(T=t_5, p=p_5)

print(t_5, h_5, e_5, s_5, v_5)