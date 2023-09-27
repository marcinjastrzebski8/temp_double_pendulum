import matplotlib.pyplot as plt
import pandas as pd
from abstract_draw import AbstractDraw

"""
Angle vs time plots (user can choose either to plot angle 1 or 2).
"""

class Draw_angle(AbstractDraw):
    def draw(self,choice = 0):
        if choice ==0:
            for point in range(len(self.time)):
                self.x.append(self.time[point])
                self.y.append(self.data['ANGLE 1'][point])
            plt.plot(self.x,self.y)
            self.x = []
            self.y = []
        else:
            for point in range(len(self.time)):
                self.x.append(self.time[point])
                self.y.append(self.data['ANGLE 2'][point])
            plt.plot(self.x,self.y)
            self.x=[]
            self.y=[]

        
    