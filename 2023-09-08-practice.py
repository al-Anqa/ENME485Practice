import numpy
import pyromat as pm

water = pm.get('mp.H2O')
temp_1 = 273.15 + 40 #kelvin
vol = 50 / 1000 #m^3
pressure = 2 # Bar
den = water.d(T=temp_1, p=pressure)
mass = vol * den
print(mass)

temp_2 = 100 + 273.15
