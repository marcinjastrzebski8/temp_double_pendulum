import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from abstract_draw import AbstractDraw



class Draw_ham(AbstractDraw):

    """
    Class used to draw the hamiltonian over time of any simulation
    Note that I did not include any figures plotted with this program in the report,
    but I have made comments about results obtained with this class
    """

    def get_dataset(self,dataset = 'file'):
        super().get_dataset(dataset)
        self.hamiltonian = self.data['HAMILTONIAN']

    def draw(self):
        for point in range(len(self.time)):
            self.x.append(self.time[point])
            self.y.append(self.hamiltonian[point])
        plt.plot(self.x,self.y)

    