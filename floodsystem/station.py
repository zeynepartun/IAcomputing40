# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


from unittest import skip
from sqlalchemy import false, true
class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label   # ['hell','hell'] is a list  or 'hell' is string
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
    
    def location(self):
        return "River: {}   Town:  {}".format(self.river,self.town)

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        # if self.typical_range == None:
        #     return False
        # elif self.typical_range[0] < self.typical_range[1]:
        #     return True
        # else:
        #     return False        
        if type(self.typical_range) != tuple:
                data_valid = False
        else:
            high =self.typical_range[1]
            low =self.typical_range[0]
        if high < low:
            data_valid= False
        else:
            data_valid =True
        return data_valid

    def relative_water_level(self):
        if self.typical_range == None or self.latest_level == None:
           skip
        elif self.typical_range_consistent() == True:
            # print(self.latest_level)
            return (self.latest_level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])
        else:
            return None 




def inconsistent_typical_range_stations(stations):
    faulty_stations = []
    for station in stations:
        if not station.typical_range_consistent(): 
            faulty_stations.append(station.name)
    return sorted (faulty_stations)




