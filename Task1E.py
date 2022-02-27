# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from turtle import st
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    stations = build_station_list()
    print(rivers_by_station_number(stations, 9))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
