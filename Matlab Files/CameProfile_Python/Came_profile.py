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

ymin = []
ymax = []

alphamin = []
alphamax = []

xmin = []
xmax = []

d = []
alphatan = []

xtan = []
ytan = []

xsup = []
ysup = []

xcam = []
ycam = []

l = math.sqrt(l0**2 + hb**2)

"""
for i in range(len(h1a)):    
    ymin.append(h1a[i])
    ymax.append(h2a[i])
    
    alphamin[i] = math.acos((h0 - h1a[i]) / l)
    alphamax[i] = math.acos((h0 - h2a[i]) / l)

    xmin[i] = l*math.sin(alphamin[i])
    xmax[i] = l*math.sin(alphamax[i])

    d[i] = math.sqrt((xmin[i] - xmax[i]) ** 2 + (ymin[i] - ymax[i]) ** 2)
    alphatan[i] = (alphamin[i] + alphamax[i]) / 2

    xtan[i] = l*math.sin(alphatan[i])    
    ytan[i] = h0 - l*math.cos(alphatan[i])

    xsup[i] = xtan[i] + (d[i]/2)*math.cos(alphatan[i])
    xinf[i] = xtan[i] - (d[i]/2)*math.cos(alphatan[i])
    
    ysup[i] = ytan[i] + (d[i]/2)*math.sin(alphatan[i])
    yinf[i] = ytan[i] - (d[i]/2)*math.sin(alphatan[i])
    
    xcam[i] = xtan[i] + (d[i]/2 + rmin + br)*math.cos(alphatan[i])
    ycam[i] = ytan[i] + (d[i]/2 + rmin + br)*math.sin(alphatan[i])
    """


dt = 0.01    # Time increment
theta = np.arange(0, 2 * np.pi, dt) # Time coordinate during cycle
 
# Generation of the soft transition between inhale and exhale
psi1 = []
psi2 = []

for i in theta:
    
    if i < (lambda2-dpsi21/2)*2*math.pi:
        psi1.append(0)
    elif i < (lambda2+dpsi21/2)*2*math.pi:
        psi1.append(0.5 + 0.5*math.cos((i-(lambda2+dpsi21/2)*2*math.pi)/(2*dpsi21)))
    else:
        psi1.append(1)
    
    psi2.append(1-psi1[-1])


print(psi2)
print(len(psi2))


