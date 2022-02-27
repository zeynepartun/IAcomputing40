# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#import utils
from re import S

from sqlalchemy import false, true
from floodsystem.utils import sorted_by_key  # noqa

from .station import MonitoringStation
import math
import haversine
from haversine import haversine, Unit

def stations_by_distance(stations, p):
  result = []
  for station in stations:
    if isinstance(station, MonitoringStation):
        station_coordinate = station.coord
        #distance_vector = (station_coordinate[0] - p[0], station_coordinate[1] - p[1])
        #distance = math.sqrt( distance_vector(0) ** 2 + distance_vector(1) ** 2 )
        distance = haversine(station_coordinate, p, unit=Unit.KILOMETERS)
        #result.append({"station_name" : station.name, "distance" : distance})
        result.append((station.name, distance))
  return result

def stations_within_radius(stations, centre, r):
  station_distances = stations_by_distance(stations, centre)
  result = []
  for item in station_distances:
    if item[1] < r:
      result.append(item)
  return result  


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


def rivers_by_station_number(stations, N):
    river_tuple_list=[]
    river_dict=stations_by_river(stations)
    for river in river_dict:
        no_of_stations =len(river_dict[river])
        river_tuple = (river, no_of_stations)
        river_tuple_list.append(river_tuple)
    sortedlist=sorted_by_key(river_tuple_list,1, True)
    x = True   
    while x:
        if sortedlist[N][1]==sortedlist[N-1][1]:
            N=N+1
        else:
            x=False
    return sortedlist[:N]
