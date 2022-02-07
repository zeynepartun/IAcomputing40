from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
def run():
    stations = build_station_list()
    a=inconsistent_typical_range_stations(stations)
    assert type(a) == list
    for item in a:
        assert type(item) == str
    assert a == sorted(a)
run()
print ('test run succesful')
