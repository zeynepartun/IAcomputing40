from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_relative_level
from floodsystem.plot2 import *
import datetime
import matplotlib.pyplot as plt
from floodsystem.flood import *
import numpy as py


def run():
    stations = build_station_list()
    a=inconsistent_typical_range_stations(stations)
    on(baseline_images=['line_dashes'], remove_text=True,
                      extensions=['png'])
    def test_line_dashes():
        fig, ax = plt.subplots()
        ax.plot(range(10), linestyle=(0, (3, 3)), lw=5)
run()
print ('test run succesful')