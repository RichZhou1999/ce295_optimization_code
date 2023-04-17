import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
import pandas as pd
from Basic_charging_agent import Basic_charging_agent

class Navie_charing_agent(Basic_charging_agent):
    def __init__(self):
        super().__init__()

    def check_validation(self,start_time, end_time, start_soc, end_soc):
        target_charge_volumn = (end_soc - start_soc) * self.battery_volumn
        if target_charge_volumn > self.I_max * (end_time - start_time)*self.step:
            return False
        return True

    def get_total_emission_value(self, start_time, end_time, start_soc, end_soc):
        validation = self.check_validation(start_time, end_time, start_soc, end_soc)
        if not validation:
            return -1
        emission_volume = 0
        current_soc = start_soc
        current_time = start_time
        while current_soc < end_soc and current_time < end_time:
            if self.R == 0:
                current = self.Power / self.voltage
            else:
                current = (-self.voltage + np.sqrt(self.voltage*self.voltage + 8*self.R*self.Power))/(4*self.R)

            if (current_soc + current * self.step / self.battery_volumn)  > end_soc:
                current = (end_soc - current_soc)*self.battery_volumn/self.step

            temp_power = current * self.voltage + current**2*self.R
            current_soc += current * self.step / self.battery_volumn
            emission_volume += temp_power * self.emission_array[current_time]
            print(self.Power)
            current_time += 1

        print(emission_volume - self.Power * self.emission_array[current_time])
        return emission_volume




n = Navie_charing_agent()
print(n.get_total_emission_value(144, 288, 0.216, 0.72))
