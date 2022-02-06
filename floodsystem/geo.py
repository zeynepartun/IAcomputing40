# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from .station import MonitoringStation
import math
import haversine
from haversine import haversine, Unit

def stations_by_distance(stations, p):
  result = []
  for station in stations:
    if isinstance(station, MonitoringStation):
      station_coordinate = station.coord
      # distance_vector = (station_coordinate[0] - p[0], station_coordinate[1] - p[1])
      # distance = math.sqrt( distance_vector(0) ** 2 + distance_vector(1) ** 2 )
      distance = haversine(station_coordinate, p, unit=Unit.KILOMETERS)
      # result.append({"station_name" : station.name, "distance" : distance})
      result.append((station.name, distance))
  return result

def stations_within_radius(stations, centre, r):
  station_distances = stations_by_distance(stations, centre)
  result = []
  for item in station_distances:
    if item[1] < r:
      result.append(item)
  return result  


      




