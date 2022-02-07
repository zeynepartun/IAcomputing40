from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
from floodsystem.utils import *
def run():
    stations = build_station_list()
    a=rivers_by_station_number(stations, 9)
    assert type(a) == list
    for item in a:
        assert type(item) == tuple
    assert a == sorted_by_key(a, 1, True)
run()
print ('test run succesful')
