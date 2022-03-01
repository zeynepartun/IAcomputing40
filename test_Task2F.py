from this import d
from floodsystem.station import *
from floodsystem.flood import *
from floodsystem.stationdata import *

from dataclasses import replace
import datetime
# from os import remove
import matplotlib.pyplot as plt
# from pytest import skip
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
# from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_relative_level
from floodsystem.plot import plot_water_levels
import numpy as np
import random
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_relative_level
from floodsystem.plot2 import *
import datetime
import matplotlib.pyplot as plt
from floodsystem.flood import *
import numpy as py


def get_test_stations():
    station1 = MonitoringStation(
        station_id=1,
        measure_id=1,
        label='Test station plot',
        coord=(float(50), float(50)),
        typical_range=(0, 1),
        river='river plot',
        town='town plot')

    station1.set_latest_level(0.5)
    return [station1]


def get_test_data():
    now = datetime.datetime.utcnow()
    dt = 1
    delta = datetime.timedelta(days=dt)
    dates = []
    levels = []
    for i in range(0, 10):
        dates.append(now - i * delta)
        levels.append(random.random())
    return dates, levels


def run():
    stations = get_test_stations()
    dates, levels = get_test_data()
    plot_water_level_with_fit(stations[0], dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
