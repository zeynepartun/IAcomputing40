# from floodsystem.geo import stations_by_distance
# from floodsystem.stationdata import build_station_list
# from floodsystem.utils import sorted_by_key

from floodsystem.station import *
from floodsystem.flood import *
from floodsystem.stationdata import *



def run():
    # Build list of stations
    stations = build_station_list()
    tol = 0.8

    # Update latest level data for all stations
    update_water_levels(stations)

    list_2B = stations_level_over_threshold(stations, tol)
    assert type(list_2B) == list
    assert list_2B == sorted_by_key(list_2B, 1, True)
    for item in list_2B:
        assert type(item) == tuple
        assert type(item[0]) == str
        assert type(item[1]) == float
        
run()   
    






