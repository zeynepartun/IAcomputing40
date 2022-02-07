from sre_constants import ASSERT
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation
from floodsystem.utils import *


station1 = MonitoringStation(
station_id=1,
measure_id=1,
label='label1',
coord=(float(50), float(50)),
typical_range='typical_range',
river='river1',
town='town1')

station2 = MonitoringStation(
station_id=2,
measure_id=2,
label='label2',
coord=(float(0.1), float(0.1)),
typical_range='typical_range',
river='river2',
town='town2')

station3 = MonitoringStation(
station_id=3,
measure_id=3,
label='label3',
coord=(float(0), float(0)),
typical_range='typical_range',
river='river3',
town='town3')

stations = [station1, station2, station3]
def test_stations_within_radius(stations):

    centre = (0, 0)
    r = 20
    result = stations_within_radius(stations, centre, r)
    sorted_result = sorted_by_key(result, 0)


    assert type(sorted_result) == list
    assert len(sorted_result) == 2
    assert sorted_result[0][0] == "label2"
    assert sorted_result[1][0] == "label3"
    print("All ran successfully")

test_stations_within_radius(stations)


