import re
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.utils import sorted_by_key


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    result = stations_within_radius(stations, centre, r)
    sorted_result = sorted_by_key(result, 0)
    for item in sorted_result:
        print(item[0])
    


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IC Flood Warning System ***")
    run()    



