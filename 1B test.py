from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
import numpy as np

def test_stations_by_distance():

    stations = build_station_list()
    p = np.random.rand(2)
    list_test_1B = stations_by_distance(stations, p)
    list_test_1B = sorted_by_key(list_test_1B, 1)


    assert len(list_test_1B) == len(stations)
    # shows all stations
    
    for x in range(len(list_test_1B)-1):
        assert (list_test_1B[x])[1] <= (list_test_1B[x+1])[1]
    # increasing order
 

    assert type(list_test_1B) == list
    print("Test ran successfully")
test_stations_by_distance()  





