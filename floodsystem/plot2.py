# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from numpy import diff


from turtle import color
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
import matplotlib


def plot_water_levels(station, dates, levels):

    # print(dates)
    plt.plot(dates, levels)
    deriv = dates.diff(levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('dates')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(station.typical_range[0], linestyle='--', color='red')
    plt.axhline(station.typical_range[1], linestyle='--', color='red')

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    levels_polyfit = polyfit(dates, levels, p)[0](matplotlib.dates.date2num(dates) - polyfit(dates, levels, p)[1])
    plt.plot(dates, levels_polyfit, color='orange')
    plt.plot(dates, levels, color='blue')
    plt.xlabel('dates')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(station.typical_range[0], linestyle='--', color='red')
    plt.axhline(station.typical_range[1], linestyle='--', color='red')

    plt.tight_layout()

    plt.show()


def derivitive_of_plot(levels,dates,station):
    if len(dates) != 0:
        deltalevel=(levels[0]-levels[1])
        deltatime=((dates[0]-dates[1]).total_seconds())/(60*15)
        temp_tuple = (station, deltalevel/deltatime)
        print(temp_tuple)
        return temp_tuple
    else:
        return(station, 0)

