import numpy as np
import pyromat as pm

water = pm.get('mp.H2O')

triple = water.triple()
print(triple)
