# from floodsystem.geo import stations_by_distance
# from floodsystem.stationdata import build_station_list
# from floodsystem.utils import sorted_by_key

from floodsystem.station import *
from floodsystem.flood import *
from floodsystem.stationdata import *

def get_test_stations():
    station1 = MonitoringStation(
    station_id=1,
    measure_id=1,
    label='label1',
    coord=(float(50), float(50)),
    typical_range=(0, 1),
    river='river1',
    town='town1')

    station2 = MonitoringStation(
    station_id=2,
    measure_id=2,
    label='label2',
    coord=(float(0.1), float(0.1)),
    typical_range=(0, 1),
    river='river2',
    town='town2')

    station3 = MonitoringStation(
    station_id=3,
    measure_id=3,
    label='label3',
    coord=(float(0), float(0)),
    typical_range=(0, 2),
    river='river3',
    town='town3')

    station1.set_latest_level(0.5)
    station2.set_latest_level(0.9)
    station3.set_latest_level(1.5)

    return [station1, station2, station3]



def run():
    # Build list of stations
    stations = get_test_stations()
    tol = 0.8

    list_2B = stations_level_over_threshold(stations, tol)
    assert len(list_2B) == 1
    assert type(list_2B) == list
    assert list_2B == sorted_by_key(list_2B, 1, True)
    for item in list_2B:
        assert type(item) == tuple
        assert type(item[0]) == str
        assert type(item[1]) == float

    print("test ran successfully")
        
run()   
    






