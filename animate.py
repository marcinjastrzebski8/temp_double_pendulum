import numpy as np
import math
from Oscillator_class import Oscillator
from System import System
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

"""
This program can animate any run that is saved using Save_Pandas
"""

readout = pd.read_pickle('beats_10.csv')

len1 = readout['PENDULUM INFO'][0]['l1']
len2 = readout['PENDULUM INFO'][0]['l2']
m1 = readout['PENDULUM INFO'][0]['m1']
m2 = readout['PENDULUM INFO'][0]['m2']
x1vals=[]
y1vals=[]
x2vals=[]
y2vals=[]
timestep = readout['TIME'][1] #first entry in time tells us what the timestep of the RK is

for i in range(len(readout['TIME'])):

    x1 = len1*np.sin(readout['ANGLE 1'][i])
    x2 = x1 + len2*np.sin(readout['ANGLE 2'][i])
    y1 = -len1*np.cos(readout['ANGLE 1'][i])
    y2 = y1-len2*np.cos(readout['ANGLE 2'][i])

    x1vals.append(x1)
    x2vals.append(x2)
    y1vals.append(y1)
    y2vals.append(y2)


fig = plt.figure()
ax = plt.axes(xlim=(-(len1+len2),(len1+len2)),ylim = (-(len1+len2),(len1+len2)))

line1, = ax.plot([],[])
line2, = ax.plot([],[])
point1, = ax.plot([],[],'bo',markersize = m1)
point2, = ax.plot([],[],'ro',markersize = m2)

def animate(frame):
    """
    This function defines what is being drawn on each frame
    After the 100th frame, some of the past positions of the bobs are also being plotted
    to obtain a sort of trail for aesthetic purposes
    """

    if frame <=100:
        line1.set_data([0,x1vals[frame]],[0,y1vals[frame]])
        line2.set_data([x1vals[frame],x2vals[frame]],[y1vals[frame],y2vals[frame]])
        point1.set_data(x1vals[frame:0:-20],y1vals[frame:0:-20])
        point2.set_data(x2vals[frame:0:-20],y2vals[frame:0:-20])
    if frame >= 100:
        line1.set_data([0,x1vals[frame]],[0,y1vals[frame]])
        line2.set_data([x1vals[frame],x2vals[frame]],[y1vals[frame],y2vals[frame]])
        point1.set_data(x1vals[frame:frame-100:-20],y1vals[frame:frame-100:-20])
        point2.set_data(x2vals[frame:frame-100:-20],y2vals[frame:frame-100:-20])

    return (line1,line2,point1,point2)
    

anim = animation.FuncAnimation(fig,animate,frames=len(x1vals),interval = timestep*1000)  #interval should be RK step * 1000 for real motion

anim.save('beats_10.mp4')
