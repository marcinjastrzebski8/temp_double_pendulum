import matplotlib.pyplot as plt
from abs_draw_bob_paths import Draw_bob
from abs_draw_angle import Draw_angle
from Save_Pandas import SavePandas
import numpy as np
import pandas as pd

"""
This program was used to illustrate the initial conditions sensitivity of the double pendulum
"""

sys = SavePandas(1,1,1,1)
sys.simulation(10000,0.001,[np.pi/2,1.9,0,0])
sys.save_as('path_uno')
sys.Sys.set_initial([0,0,0,0])
sys.simulation(10000,0.001,[np.pi/2,1.905,0,0])
sys.save_as('path_dos')

mypath1 = Draw_bob()
mypath1.get_dataset('path_uno.csv')
mypath1.name_axes('x','y')
mypath1.draw()
mypath1.x = []
mypath1.y = []
mypath1.get_dataset('path_dos.csv')
mypath1.draw()
plt.legend([R'$\theta_{2,0} = 1.9$',R'$\theta_{2,0} = 1.905$'])
plt.show()

myangle1 = Draw_angle()
myangle1.get_dataset('path_uno.csv')
myangle1.name_axes('Time (s)',R'$\theta_2$ (rad)')

myangle1.draw(1)
myangle1.x = []
myangle1.y =[]
myangle1.get_dataset('path_dos.csv')
myangle1.draw(1)
plt.legend([R'$\theta_{2,0} = 1.9$',R'$\theta_{2,0} = 1.905$'])
plt.show()





