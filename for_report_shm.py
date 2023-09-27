from abs_draw_angle import Draw_angle
from Save_Pandas import SavePandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""
This shows the code reproduces simple harmonic motion
"""


shm = SavePandas(10**(-4),1,0.5,0.5)
shm.simulation(10000,0.001,[0.1,0.1,0,0])
shm.save_as('shm')
dat = pd.read_pickle('shm.csv')
T = 2*np.pi*np.sqrt(1/10) #the theoretical period 
#of the simple pendulum we've created
x = np.arange(0,10,0.001)
y = 0.1*np.cos((2*np.pi/T)*x)
draw = Draw_angle()
draw.name_axes('Time (s)',R'$\theta_{2}$ (rad)')
draw.get_dataset('shm.csv')
draw.draw(1)
plt.plot(x,y,linestyle = 'dashed',linewidth = 2,label = 'prediction')
plt.legend(['Simulation','Theory'],loc=1)
draw.show()
