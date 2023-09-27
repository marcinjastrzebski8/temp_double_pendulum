from abc import ABC, abstractmethod
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

class AbstractDraw(ABC):

    """
    This is an abstract class to make drawing plots quicker for the purpose of the analysis.
    get_dataset uses DataFrames saved with Save_Pandas that are common for all the classes derived from this one
    What is being drawn is the abstract part of this class and is to be defined for each subclass
    """

    def __init__(self):
        self.x = []
        self.y = []
        self.fig, self.ax = plt.subplots()
        super().__init__()

    def name_axes(self,xname='xname',yname='yname'):
        self.ax.set_xlabel(xname)
        self.ax.set_ylabel(yname)

    def get_dataset(self,dataset = 'file'):
        self.data = pd.read_pickle(dataset)
        self.time = self.data['TIME']
        self.timestep = self.data['TIME'][1]
        self.l1 = self.data['PENDULUM INFO'][0]['l1']
        self.l2 = self.data['PENDULUM INFO'][0]['l2']
        self.m1 = self.data['PENDULUM INFO'][0]['m1']
        self.m2 = self.data['PENDULUM INFO'][0]['m2']

    @abstractmethod
    def draw(self):
        pass

    def show(self):
        plt.show()
