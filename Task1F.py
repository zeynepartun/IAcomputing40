# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from turtle import st

from pyrsistent import inc
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    stations = build_station_list()
    print(inconsistent_typical_range_stations(stations))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

