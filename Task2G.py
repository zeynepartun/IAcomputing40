from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_relative_level
from floodsystem.plot2 import *
import datetime
import matplotlib.pyplot as plt
from floodsystem.flood import *
import numpy as py
from floodsystem.station import MonitoringStation


def run():
    stations=build_station_list()
    update_water_levels(stations)
    N=6
    stations_N = (stations_highest_relative_growth(stations, N))
    list=[]
    listd=[]
    for i in stations_N:
        list.append(i[0])
    list_1 = []
    for station in stations:
        if station.name in list:
            list_1.append(station)

    for station in list_1:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        #if len(dates) == 0:
            #print(station.name, 'data error')
        #else:
            #print(sorted_by_key(list, 1, reverse=True)[:N])
        station, deriv = (derivitive_of_plot(levels,dates,station))
        if len(dates) != 0:
            levl = (station.relative_water_level())
            a=1
            b=1000
            risk = a*levl + b*deriv
            print(risk)
            if risk>5:
                print('severe')
            elif risk>3:
                print('high')
            elif risk>-3:
                print('moderate')
            else:
                print('low')
                
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

