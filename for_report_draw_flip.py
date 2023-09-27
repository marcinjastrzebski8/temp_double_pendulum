import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from collections import OrderedDict

"""
This program draws the data saved with for_report_flip
"""


flipdata = pd.read_pickle('ttf_full_0_002_long_abs.csv')

ang1 = flipdata['ANGLE 1']
ang2 = flipdata['ANGLE 2']

fig, ax1 = plt.subplots()
ax1.set_xlabel(R'$\theta_{1}$')
ax1.set_ylabel(R'$\theta_{2}$')


c = flipdata['TIME TO FLIP']

plt.scatter(ang1,ang2,s = 0.5,c=c,cmap='PuBu_r',norm=matplotlib.colors.LogNorm()) #the scatterplot with a color map

cbar = plt.colorbar()
cbar.set_label('Time to flip (s)')
plt.show()

"""
This part of the program deals with the assumption that there is a symmetry wrt to the origin
"""

diff = []
count = 0 #to see how many points were not symmetric (divide by two because they come in pairs)

for point in range(len(c)):

    """
    This loop compares the points on opposite ends of the list of time to flip for each of the points
    (Which happen to correspond to points on the opposite sides of the origin on the map)
    """
    error = abs(c[point]-c[len(c)-1-point])
    if error == 0:
        diff.append(error)
    else:
        count += 1
        rel_error = error/point
        diff.append(rel_error*100)


plt.scatter(ang1,ang2,s = 0.5,c=diff,cmap='PuBu_r',norm=matplotlib.colors.LogNorm())
cbar = plt.colorbar()
cbar.set_label('Error(%)')
plt.xlabel(R'$\theta_{1}$')
plt.ylabel(R'$\theta_{2}$')
plt.show()
print(count)


