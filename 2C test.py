

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *



def run():
    # Build list of stations
    stations = build_station_list()
    tol = 0.8

    # Update latest level data for all stations
    update_water_levels(stations)

    list_2C = stations_highest_relative_level(stations, 10)
    assert type(list_2C) == list
    assert list_2C == sorted_by_key(list_2C, 1, True)
    for item in list_2C:
        assert type(item[0]) == str
        assert type(item[1]) == float 

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
