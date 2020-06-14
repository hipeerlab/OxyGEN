"""
Code to determine the Came profile 
"""
import numpy as np
import matplotlib.pyplot as plt 
import math

# GEOMETRICAL PARAMETERS 
l0 = 27.5   # Length from the bearing to the hinge 
h0 = 6.5    # Length of the vertical wall which supports the finge
hb = 4.0    # Length of the vertical support of the bearing 
br = 1.1    # Bearing radius 

# max and min positions of the bearing
h1a = [6.5, 7.1, 7.7, 8.3, 8.9]
h2a = [20.5, 20.5, 20.5, 20.5, 20.5]

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

 
def geometry_generation(h1a, h2a, h0, hb):
    
    l = math.sqrt(l0**2 + hb**2)

    ymin = h1a
    ymax = h2a

    alphamin = math.acos((h0 - h1a) / l)
    alphamax = math.acos((h0 - h2a) / l)

    xmin = l*math.sin(alphamin)
    xmax = l*math.sin(alphamax)

    d = math.sqrt((xmin - xmax) ** 2 + (ymin - ymax) ** 2)
    alphatan = (alphamin + alphamax) / 2

    xtan = l*math.sin(alphatan)    
    ytan = h0 - l*math.cos(alphatan)

    xsup = xtan + (d/2)*math.cos(alphatan)
    xinf = xtan - (d/2)*math.cos(alphatan)
    
    ysup = ytan + (d/2)*math.sin(alphatan)
    yinf = ytan - (d/2)*math.sin(alphatan)
    
    xcam = xtan + (d/2 + rmin + br)*math.cos(alphatan)
    ycam = ytan + (d/2 + rmin + br)*math.sin(alphatan)
    
    return [xtan, ytan]

a = geometry_generation(h1a[1], h2a[1], h0, hb)
print(a)
print(type(a))



