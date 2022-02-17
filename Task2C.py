

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *



def run():
    # Build list of stations
    stations = build_station_list()
    tol = 0.8

    # Update latest level data for all stations
    update_water_levels(stations)

    list_2C = stations_highest_relative_level(stations, 10)
    for item in list_2C:
        print(item[0], item[1])
        
    

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
