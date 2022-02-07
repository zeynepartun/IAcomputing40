from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    stations = build_station_list()
    a=rivers_with_station(stations)
    assert type(a) == list
    
    b=stations_by_river(stations)
    assert type(b) == dict
    assert len(a) == len(b)
    for key in b:
        object = b[key]
        assert type(b[key]) == list
run()
print ('test run succesful')
