# Copyright (C) 2018 Garth N. Wells
# SPDX-License-Identifier: MIT

from turtle import st
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    stations = build_station_list()
    list_of_rivers = sorted(rivers_with_station(stations))
    print (list_of_rivers[:10])
    #print(sorted(rivers_with_station(stations))[:10])


    river_dict = stations_by_river(stations)
    wanted_river = ['River Aire', 'River Cam', 'River Thames']
    for river in river_dict:
        if river in wanted_river:
            station_list = []
            for station in river_dict[river]:
                station_list.append(station.name)
            print(river,sorted(station_list))    

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
