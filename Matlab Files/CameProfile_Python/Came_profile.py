"""
Code to determine the Came profile 
"""
import numpy as np
import matplotlib.pyplot as plt 

# GEOMETRICAL PARAMETERS 
l0 = 27.5   # Length from the bearing to the hinge 
h0 = 6.5    # Length of the vertical wall which supports the finge
hb = 4.0    # Length of the vertical support of the bearing 
br = 1.1    # Bearing radius 

# max and min positions of the bearing
h1a = np.array([6.5, 7.1, 7.7, 8.3, 8.9])
h2a = np.array([20.5, 20.5, 20.5, 20.5, 20.5])

nc = 1    # Cycles per cam turn (1 to 3)
rmin = 5  # Minimum radius of the camshaft 

# BREATHING CYCLE PARAMETERS  
lambda1 = 0.5    # Duration inhale cycle
lambda2 = 0.04   # Duration of the whole cycle 

dpsi21 = 0.05   # Soft transition - inhale exhale cycle
dpsi12 = 0.04   # Soft transition - inhale exhale cycle

# Adjust parameters inhale curve 
ga1 = 3.1
gb1 = .85
ff1 = 50

# Adjust parametes exhale curve
ga2 = 3.1
gb2 = .80
ff2 = 50

#####################################################
# GENERATION OF THE CURVES AND THE CAMSHAFT


def quadrado(num):
    return num ** 2

print(quadrado(h1a))




