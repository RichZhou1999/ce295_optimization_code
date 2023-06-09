import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
import pandas as pd

class Basic_charging_agent():
    def __init__(self):
        self.voltage = 400  # nominal_voltage
        self.battery_volumn = 60 * 1000 / 400  # Q = kWh / v
        self.emission_max_value = 100
        self.Power = 10 * 1000  # power of the charger
        self.I_max = self.Power / self.voltage
        self.R = 0.0001  # resistance
        self.Power_limit = 10 * 1000  # simple assumption to the limit of the power: 100 kw
        self.Power_limit_slope_line_Intercept = 50 * 1000  # simple assumption to the limit of the power(the sloped line): 100 kw
        self.action_interval = 5
        self.step = self.action_interval / 60  # 10(min)/ 60(min)
        self.maximum_steps = int(24 / self.step * 2)  # 24 hours divided by step
        x = np.linspace(0, int(self.maximum_steps / 2), int(self.maximum_steps / 2) + 1)
        emission_array = self.emission_max_value / ((self.maximum_steps / 2 / 2) ** 2) * (x - (self.maximum_steps / 2 / 2)) ** 2
        self.emission_array = np.concatenate((emission_array[:-1], emission_array[:-1]), axis=0)
