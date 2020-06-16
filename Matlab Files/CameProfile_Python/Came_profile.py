"""
Code to determine the Came profile 
"""
import numpy as np
import matplotlib.pyplot as plt 
import math
from scipy.stats import gamma

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

# Generation of the geometry
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
xinf = []

ysup = []
yinf = []

xcam = []
ycam = []

l = math.sqrt(l0**2 + hb**2)

for i in range(len(h1a)):    
    ymin.append(h1a[i])
    ymax.append(h2a[i])
    
    alphamin.append(math.acos((h0 - h1a[i]) / l))
    alphamax.append(math.acos((h0 - h2a[i]) / l))

    xmin.append(l*math.sin(alphamin[i]))
    xmax.append(l*math.sin(alphamax[i]))

    d.append(math.sqrt((xmin[i] - xmax[i]) ** 2 + (ymin[i] - ymax[i]) ** 2))
    alphatan.append((alphamin[i] + alphamax[i]) / 2)

    xtan.append(l*math.sin(alphatan[i]))
    ytan.append(h0 - l*math.cos(alphatan[i]))

    xsup.append(xtan[i] + (d[i]/2)*math.cos(alphatan[i]))
    xinf.append(xtan[i] - (d[i]/2)*math.cos(alphatan[i]))
    
    ysup.append(ytan[i] + (d[i]/2)*math.sin(alphatan[i]))
    yinf.append(ytan[i] - (d[i]/2)*math.sin(alphatan[i]))
    
    xcam.append(xtan[i] + (d[i]/2 + rmin + br)*math.cos(alphatan[i]))
    ycam.append(ytan[i] + (d[i]/2 + rmin + br)*math.sin(alphatan[i]))

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

#############################################################
# Generation of the complete breathing cycle rho(theta)

rho = []
rho1 = []
rho2 = []
rho1next = []
rho2next = []

rhomin = 1000
rhomax = 0

for i in range(len(theta)):

    # Inhale curve 
    rho1.append(ff1*gamma.pdf(theta[i], ga1, scale=gb1))
    rho1next.append(ff1*gamma.pdf(theta[i]+2*math.pi, ga1, scale=gb1))

    # Exhale curve
    rho2.append(ff2*gamma.pdf(theta[i], ga2, scale=gb2))
    rho2next.append(ff2*gamma.pdf(theta[i]+2*math.pi, ga2, scale=gb2))

    rho.append(max(rho1[i], rho1next[i]))

    # Capturing min and max in order to generate the normalized curve
    if rho[i] > rhomax:
        rhomax = rho[i]

    if rho[i] < rhomin:
        rhomin = rho[i]

# Generation of a normalized curve and camshaft
rhonorm = []
rhocam = np.zeros(shape=(len(d), len(theta)))

for i in range(len(theta)):
    rhonorm.append((rho[i]-rhomin)/(rhomax-rhomin))

    for n in range(len(d)):
        rhocam[n, i] = rmin + rhonorm[i] * d[n]

# Generation of the first derivative of the camshaft geometry to analize and
# validate the design

drho = np.zeros(len(rho))
drhonorm = np.zeros(len(rho))
drhocam = np.zeros(np.size(rhocam))

a = rmin
b = 1/dt

for i in range(len(rho)-1):
    drho[i] = (b * (rho[i+1] -rho[i]))
    drhonorm[i] = (b * (rhonorm[i+1] - rhonorm[i]))
    drhocam[i] = b * (rhocam.T.item(i+1)-rhocam.T.item(i)) + a

drho[len(rho) - 1] = b * (rho[0]-rho[len(rho) - 1])
drhonorm[len(rhonorm) - 1] = b * (rhonorm[0] - rhonorm[len(rhonorm) - 1])
drhocam[np.size(rhocam) - 1] = b * (rhocam.item(0) - rhocam.item(np.size(rhocam) - 1)) + a

print(drhocam[-1])
print('Eba')

"""

"""


