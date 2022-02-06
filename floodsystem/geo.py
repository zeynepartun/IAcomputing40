# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from floodsystem.utils import sorted_by_key  # noqa
#1d
def rivers_with_station(stations):
    rivers=[]
    for station in stations:
        if station.river not in rivers:
            rivers.append(station.river)
    return rivers

def stations_by_river(stations):
    river_dict = {}
    rivers = rivers_with_station(stations)
    #key is name, object is a list of stations
    for river in rivers:
        key = river
        object= []
        for station in stations:
            if station.river == river:
                object.append(station)
        river_dict[key]=object
    return river_dict
