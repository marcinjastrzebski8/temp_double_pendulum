import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from abstract_draw import AbstractDraw

class Draw_bob(AbstractDraw):

    """
    Class used to draw the paths (in physical space)
    taken by the second bob
    Plotting the first bob instead could easily be achieved
    by appending x1 and y1
    """

    def draw(self):
        for point in range(len(self.time)):
            x1 = self.l1*np.sin(self.data['ANGLE 1'][point])
            x2 = x1 + self.l2*np.sin(self.data['ANGLE 2'][point])
            y1 = -self.l1*np.cos(self.data['ANGLE 1'][point])
            y2 = y1-self.l2*np.cos(self.data['ANGLE 2'][point])
            self.x.append(x2)
            self.y.append(y2)
        plt.plot(self.x,self.y)

    